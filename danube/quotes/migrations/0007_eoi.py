# Generated by Django 4.1 on 2022-08-22 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0009_auto_20220731_1816"),
        ("quotes", "0006_alter_rfqbusinessrequest_unique_together"),
    ]

    operations = [
        migrations.CreateModel(
            name="EOI",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.PositiveIntegerField(
                        choices=[(1, "NEW"), (2, "ACCEPTED"), (3, "REJECTED")],
                        default=1,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "business",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="eoi",
                        to="profiles.businessdetails",
                    ),
                ),
                (
                    "rfq",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="eoi",
                        to="quotes.rfq",
                    ),
                ),
            ],
        ),
    ]
