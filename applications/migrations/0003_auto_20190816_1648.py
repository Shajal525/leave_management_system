# Generated by Django 2.2.4 on 2019-08-16 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20190816_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='leave_end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='leave_start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
