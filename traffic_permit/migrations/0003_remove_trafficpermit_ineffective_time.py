# Generated by Django 3.0 on 2019-12-17 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_permit', '0002_auto_20191217_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trafficpermit',
            name='ineffective_time',
        ),
    ]
