# Generated by Django 3.2.6 on 2021-11-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopify',
            name='record_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
