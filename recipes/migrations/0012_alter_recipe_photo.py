# Generated by Django 4.1.5 on 2023-01-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_alter_recipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]