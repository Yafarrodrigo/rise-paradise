from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100, null=True)
    photo = models.CharField(null=False,max_length=255, default="https://cookimia.com/wp-content/uploads/2012/11/arroz.jpg")
    ingredients = models.TextField(null=True)
    created = models.DateTimeField(default=now, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name