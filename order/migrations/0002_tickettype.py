# Generated by Django 4.0.6 on 2022-07-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TicketType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=55, unique=True)),
                ("price", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
