# Generated by Django 3.0.5 on 2021-10-18 10:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favorites',
            new_name='Favorite',
        ),
        migrations.AlterField(
            model_name='ingredientinrecipe',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients_amount', to='api.Ingredient', verbose_name='Ингредиент'),
        ),
        migrations.AlterField(
            model_name='ingredientinrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients_amount', to='api.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Не менее 1')], verbose_name='Время приготовления'),
        ),
        migrations.AlterUniqueTogether(
            name='ingredientinrecipe',
            unique_together=set(),
        ),
    ]
