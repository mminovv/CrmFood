# Generated by Django 3.1 on 2020-09-04 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20200904_1954'),
        ('user', '0007_auto_20200904_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.roles'),
        ),
    ]
