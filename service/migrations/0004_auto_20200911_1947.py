# Generated by Django 3.1 on 2020-09-11 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20200911_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealtoorders',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.orders'),
        ),
    ]