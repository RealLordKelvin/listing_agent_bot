# Generated by Django 4.0.1 on 2022-06-01 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='pub_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 11, 43, 25, 636476, tzinfo=utc)),
        ),
    ]
