# Generated by Django 4.1.5 on 2023-01-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='ingredientes...'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='Nueva receta', max_length=100),
        ),
    ]
