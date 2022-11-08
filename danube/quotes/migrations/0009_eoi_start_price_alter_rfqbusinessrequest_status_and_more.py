# Generated by Django 4.1 on 2022-08-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0009_auto_20220731_1816"),
        ("quotes", "0008_eoi_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="eoi",
            name="start_price",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="rfqbusinessrequest",
            name="status",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "WAITING"),
                    (2, "CLOSED"),
                    (3, "ARCHIVED"),
                    (4, "DECLINED"),
                ],
                default=1,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="eoi", unique_together={("rfq", "business")},
        ),
    ]