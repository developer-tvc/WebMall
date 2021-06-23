from django.core.mail import send_mail
from decouple import config


def send_mail_without_celery():
    send_mail('CELERY', "CELERY IS COOL",
              config('EMAIL_HOST_USER'),
              [config('EMAIL_TO')],
              fail_silently=False
              )
    return None
