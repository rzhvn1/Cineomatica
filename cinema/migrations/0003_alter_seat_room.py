# Generated by Django 4.0.6 on 2022-07-06 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0002_seat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seat",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="seat",
                to="cinema.room",
            ),
        ),
    ]
