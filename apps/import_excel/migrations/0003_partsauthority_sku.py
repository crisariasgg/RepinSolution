# Generated by Django 3.2.6 on 2021-11-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel', '0002_shopify_record_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='partsauthority',
            name='sku',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='SKU'),
        ),
    ]
