from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives

class Email():

    @classmethod
    def send_email(cls, email_template, email_subject, email_id):


        email_obj = EmailMultiAlternatives(
            email_subject, 
            email_subject,
            settings.EMAIL_HOST_USER, 
            [email_id],
            )
        email_obj.attach_alternative(email_template, 'text/html')
        email_obj.send()       

        
