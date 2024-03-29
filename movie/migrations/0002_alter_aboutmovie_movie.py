# Generated by Django 4.0.6 on 2022-07-05 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutmovie",
            name="movie",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="about_movie",
                to="movie.movie",
            ),
        ),
    ]
