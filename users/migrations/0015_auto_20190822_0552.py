# Generated by Django 2.2.4 on 2019-08-22 05:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20190822_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='on_leave_till',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 8, 22, 5, 52, 1, 890505, tzinfo=utc)),
        ),
    ]
