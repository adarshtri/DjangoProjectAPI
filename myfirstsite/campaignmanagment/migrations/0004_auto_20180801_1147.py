# Generated by Django 2.0.7 on 2018-08-01 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('campaignmanagment', '0003_auto_20180801_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 1, 6, 17, 15, 176834, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 1, 6, 17, 15, 176857, tzinfo=utc)),
        ),
    ]
