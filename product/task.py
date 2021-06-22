from celery import shared_task
from time import sleep
from decouple import config
from django.core.mail import send_mail

@shared_task
def sleepy():
    sleep.delay(2)
    return None


@shared_task
def send_mail_task():
    send_mail('CELERY', "CELERY IS COOL",
              config('EMAIL_HOST_USER'),
              [config('EMAIL_TO')],
              fail_silently=False
              )
    return None
