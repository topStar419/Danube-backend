# Generated by Django 4.1 on 2022-08-15 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0009_auto_20220731_1816"),
        ("quotes", "0004_alter_rfq_status_rfqbusinessrequest"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rfq",
            name="property",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rfq",
                to="profiles.property",
            ),
        ),
    ]