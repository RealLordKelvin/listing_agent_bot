# Generated by Django 4.0.1 on 2022-06-01 11:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_price_alter_listing_pub_update'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='listing',
            unique_together={('reference_number',)},
        ),
        migrations.AlterField(
            model_name='listing',
            name='pub_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 11, 45, 4, 383105, tzinfo=utc)),
        ),
    ]
