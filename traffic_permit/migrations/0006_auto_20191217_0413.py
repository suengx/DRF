# Generated by Django 3.0 on 2019-12-17 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_permit', '0005_unit_unit_principal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficpermit',
            name='unit',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='traffic_permits', to='traffic_permit.Unit', verbose_name='所属单位'),
        ),
    ]
