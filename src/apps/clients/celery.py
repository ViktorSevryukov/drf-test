import os
import sys

from celery import Celery
from django.conf import settings

sys.path.append('..')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

app = Celery('clients', broker='amqp://guest:guest@localhost:5672//',
             backend='amqp://')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
