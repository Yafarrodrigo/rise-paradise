from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to="", default="media/guest-user_clv1cg_jztgdi")

    def __str__(self):
        return str(self.user)

class Recipe(models.Model):
    name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to="", default="media/X43pV3x_flek8a")
    ingredients = models.TextField(null=True)
    preparation = models.TextField(null=True)
    created = models.DateTimeField(default=now, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name