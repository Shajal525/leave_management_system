# Generated by Django 2.2.4 on 2019-08-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20190822_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='on_leave_till',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
