# Generated by Django 2.2.4 on 2019-08-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20190822_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='on_leave_till',
            field=models.DateField(auto_now_add=True),
        ),
    ]
