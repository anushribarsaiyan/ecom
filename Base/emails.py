from django.conf import settings
from django.core.mail import send_mail


def send_account_actrivation_email(email,email_token):
    subject = "your account needs to be verified"
    email_form = settings.EMAIL_HOST_USER
    print(email_token )
    message = f'Hi click on the link to activate your account http://127.0.0.1:8000/account/activate/{email_token}'
    send_mail(subject , message , email_form, [email])
