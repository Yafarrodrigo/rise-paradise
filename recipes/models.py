from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100, default="Nueva receta")
    ingredients = models.TextField(blank=False, default="ingredientes...")
    created = models.DateTimeField(default=now, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name