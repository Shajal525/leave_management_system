# Generated by Django 2.2.4 on 2019-08-16 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationmodel',
            name='status',
            field=models.CharField(default='panding', max_length=100),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='leave_end_date',
            field=models.DateField(default=datetime.date(2019, 8, 16)),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='leave_start_date',
            field=models.DateField(default=datetime.date(2019, 8, 16)),
        ),
    ]
