# Generated by Django 3.2.3 on 2022-11-29 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipeingredientunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientunit',
            name='unit',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.unit'),
        ),
    ]
