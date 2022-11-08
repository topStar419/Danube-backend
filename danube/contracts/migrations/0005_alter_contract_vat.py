# Generated by Django 4.1 on 2022-10-12 15:04

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_remove_workitem_include_in_first_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=8, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
