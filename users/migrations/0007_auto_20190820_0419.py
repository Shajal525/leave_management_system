# Generated by Django 2.2.4 on 2019-08-20 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yearandtotalleaveavailable',
            name='current_year',
        ),
        migrations.RemoveField(
            model_name='yearandtotalleaveavailable',
            name='total_leave_available',
        ),
    ]
