# Generated by Django 4.1.5 on 2023-01-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_alter_profile_bio_alter_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
