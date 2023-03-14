import os

from celery import Celery

from dotenv import load_dotenv
load_dotenv()

# print(os.environ.get('DJANGO_SETTINGS_MODULE'))

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      os.environ.get('DJANGO_SETTINGS_MODULE'))
app = Celery('getnime')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='')
app.conf.broker_url = "redis://127.0.0.1:6379/1"

app.conf.result_backend_transport_options = {
    'retry_policy': {
        'timeout': 5.0
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
