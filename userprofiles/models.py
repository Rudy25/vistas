from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='avatars') #Pil ---> pillow
    user = models.OneToOneField(User)

    def __unicode__(selft):
        return selft.user.username

class UserTrack(models.Model):
    cont = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User)


# Create your models here.
