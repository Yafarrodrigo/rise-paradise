from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
