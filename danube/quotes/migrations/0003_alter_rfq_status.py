# Generated by Django 4.1 on 2022-08-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0002_auto_20220805_1416"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rfq",
            name="status",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "DRAFT"),
                    (2, "SAVED"),
                    (3, "OPEN"),
                    (4, "CONTRACTED"),
                    (5, "ARCHIVED"),
                    (6, "COMPLETED"),
                ],
                default=1,
            ),
        ),
    ]