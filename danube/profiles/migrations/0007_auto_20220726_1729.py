# Generated by Django 3.1.2 on 2022-07-26 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0006_businessdetails"),
    ]

    operations = [
        migrations.RenameField(
            model_name="businessdetails",
            old_name="companies_house_number",
            new_name="company_number",
        ),
    ]
