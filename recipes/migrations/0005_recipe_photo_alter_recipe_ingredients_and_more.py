# Generated by Django 4.1.5 on 2023-01-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_ingredients_alter_recipe_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.CharField(default='https://cookimia.com/wp-content/uploads/2012/11/arroz.jpg', max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
