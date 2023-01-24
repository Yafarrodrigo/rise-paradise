from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
import json
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nickname = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to="", default="media/guest-user_clv1cg_jztgdi")

    def __str__(self):
        return str(self.user)

class Recipe(models.Model):
    name = models.CharField(max_length=40, null=True)
    photo = models.ImageField(upload_to="", default="media/OIP_xf4owa")
    ingredients = models.TextField(null=True)
    description = models.TextField(null=True, blank=True)
    preparation = models.TextField(null=True)
    created = models.DateTimeField(default=now, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name