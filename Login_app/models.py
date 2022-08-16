from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    facebook_id = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture', blank=True)

    def __str__(self):
        return self.user.username
