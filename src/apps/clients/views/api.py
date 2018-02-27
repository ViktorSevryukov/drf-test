import os

from django.conf import settings
from django.db import transaction
from django.db.models import F
from django.utils.translation import ugettext_lazy as _

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from celery.result import AsyncResult

from apps.clients.models import Client
from apps.clients.tasks import export_xls
from apps.clients.celery import app


class Vote(APIView):
    """
    View to vote for client photo
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):
        """
        API for vote on client's photo, update client's rating
        :param pk: client id
        """
        try:
            with transaction.atomic():
                Client.objects.select_for_update().filter(
                    id=pk, rating__lt=Client.MAX_RATING).update(
                    rating=F('rating') + 1)
                client = Client.objects.get(id=pk)
            return Response({'rating': client.rating},
                            status=status.HTTP_200_OK)
        except:
            # if error occurs with transaction, return code 503
            return Response(data={'details': _('Please, try later')},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)


class CheckTask(APIView):
    """
    API for check task status
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, task_id, format=None):
        """
        Check task status
        :param task_id:
        """

        task = AsyncResult(id=str(task_id), app=app)

        if not task.ready():
            return Response(
                {'details': _("Report is not ready"), 'code': task.status},
                status=status.HTTP_200_OK)

        if task.successful():
            # if staus of task successfull, return url of generated .xls file

            file_name = os.path.join(settings.REPORT_URL, task.result)

            return Response(
                {'details': _("Report successfully created"),
                 'code': task.status, 'url': file_name},
                status=status.HTTP_200_OK)

        if task.failed():
            return Response(
                {'details': _("Error in task"), 'code': 'STOP'},
                status=status.HTTP_200_OK)

        return Response(
            {'details': _("Something wrong with task"), 'code': 'STOP'})


class ExportXLS(APIView):
    """
    API for export clients list to xls, start celery task
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        if not Client.objects.exists():
            return Response(
                {'details': _("Clients not found"), 'code': 'error'},
                status=status.HTTP_404_NOT_FOUND)

        task = export_xls.delay()  # call task to export

        # also return task id to check it's status later (with CheckTask API)
        return Response(
            {'details': _("Exporting in process"), 'code': 'in_progress',
             'task_id': task.id})
