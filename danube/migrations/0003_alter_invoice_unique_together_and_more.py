# Generated by Django 4.1 on 2022-10-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danube', '0002_alter_invoice_unique_together_alter_invoice_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='status_business',
            field=models.PositiveIntegerField(choices=[(1, 'OPEN'), (2, 'PENDING'), (3, 'PAID')], default=1),
        )
    ]