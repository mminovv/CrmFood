# Generated by Django 3.1 on 2020-09-05 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20200905_2331'),
        ('user', '0004_auto_20200905_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.roles'),
        ),
    ]
