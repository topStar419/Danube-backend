# Generated by Django 4.1 on 2022-10-28 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0008_contract_first_payment_paid_business'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='workitem',
            options={'ordering': ('-created_at',)},
        ),
    ]
