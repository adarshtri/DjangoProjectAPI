# Generated by Django 2.0.7 on 2018-08-01 06:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('campaignmanagment', '0002_auto_20180801_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaign_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 1, 6, 14, 12, 911423, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 1, 6, 14, 12, 911457, tzinfo=utc)),
        ),
    ]
