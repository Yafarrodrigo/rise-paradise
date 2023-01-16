# Generated by Django 4.1.5 on 2023-01-16 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='???'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='???', max_length=100),
        ),
    ]
