from django.db import models
from django.contrib.auth.models import User
from Base.model import BaseModel
from django.dispatch  import receiver
from django.db.models.signals import post_save
import uuid
from Base.emails import send_account_actrivation_email
# Create your models here.


class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile",unique=True)
    is_email_verifield = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100,null=True,blank=True)
    profile_image = models.ImageField(upload_to='profile')

@receiver(post_save, sender = User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid)
            email = instance.email
            send_account_actrivation_email(email,email_token)
    except Exception as e:
        print(e)