import logging
import os
import uuid

from django.conf import settings

from apps.clients.celery import app

from apps.clients.models import Client
from apps.clients.utils.export_xls import queryset_to_workbook

logger = logging.getLogger('celery')


@app.task
def export_xls():
    """
    Task for export clients to xls
    :return: name of created file
    """
    logger.info('Starting task for export report to xls')

    # TODO: make export for photo
    # define columns to export
    columns = ('first_name', 'last_name', 'birth_date', 'age')
    workbook = queryset_to_workbook(Client.objects.all(), columns)

    logger.info('Workbook successfully generated')

    if not os.path.exists(settings.REPORT_PATH):
        os.makedirs(settings.REPORT_PATH)

    generated_name = '{}.xls'.format(str(uuid.uuid4()))
    file_name = os.path.join(settings.REPORT_PATH, generated_name)

    workbook.save(file_name)

    logger.info('Workbook successfully saved')
    return generated_name
