# Generated by Django 3.2.6 on 2021-11-05 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel', '0003_partsauthority_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partsauthority',
            name='coreprice',
            field=models.FloatField(blank=True, null=True, verbose_name='Coreprice'),
        ),
    ]
