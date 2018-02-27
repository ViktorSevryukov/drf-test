from django.urls import path

from apps.clients.views.api import Vote, CheckTask, ExportXLS

app_name = 'clients'

urlpatterns = [
    path('<int:pk>/vote/', Vote.as_view()),
    path('export/', ExportXLS.as_view()),
    path('check_task/<uuid:task_id>/', CheckTask.as_view()),
]