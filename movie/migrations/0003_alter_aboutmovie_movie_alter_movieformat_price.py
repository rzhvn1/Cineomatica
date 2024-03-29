# Generated by Django 4.0.6 on 2022-07-05 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0002_alter_aboutmovie_movie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutmovie",
            name="movie",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="about_movie",
                to="movie.movie",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="movieformat",
            name="price",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
