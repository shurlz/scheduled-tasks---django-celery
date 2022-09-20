from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emailcampaign.settings')

app = Celery('emailcampaign')

app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat tasks registration 
app.conf.beat_schedule = {

    #  basic usage
    'print_asynchronous_steadily':{
        'task':'emailscheduler.tasks.print_async',
        'schedule': 2, #executes every two seconds
        #'args': ()
    },
    'print_asynchronous_every_5_seconds':{
        'task':'emailscheduler.tasks.five_seconds_async',
        'schedule': 5,
    },

    # sendind scheduled mail
    'Send_clients_mail': {
        'task': 'emailscheduler.tasks.schedule_mail',
        'schedule': 3000.0, 
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')