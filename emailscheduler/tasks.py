from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import gatherMails

@shared_task
def print_async():    
    print("Asychronous yeah.......")

@shared_task
def five_seconds_async():
    print("Async per five seconds...")

@shared_task
def schedule_mail():
    subject = 'mail from company name'    
    message = 'Thanks for trusting us'    
    email_from = settings.EMAIL_HOST_USER    
    recipient_list = [user.email for user in gatherMails.objects.all()]    
    send_mail( subject, message, email_from, recipient_list )    
    return "Mail has been sent........"

