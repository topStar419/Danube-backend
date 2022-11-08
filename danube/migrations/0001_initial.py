# Generated by Django 4.1 on 2022-09-20 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0002_alter_contract_description'),
        ('quotes', '0010_alter_eoi_status'),
        ('profiles', '0010_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'DRAFT'), (2, 'WAITING'), (3, 'IN_PROGRESS'), (4, 'DONE'), (5, 'REJECTED')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='profiles.businessdetails')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='contracts.contract')),
                ('eoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='quotes.eoi')),
                ('property_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='profiles.property', verbose_name='property')),
            ]
        ),
    ]