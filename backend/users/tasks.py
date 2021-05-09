from django.core import management

from medico import celery_app


@celery_app.task
def clearsessions():
    management.call_command('clearsessions')
