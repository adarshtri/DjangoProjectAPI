# Generated by Django 2.0.7 on 2018-07-31 13:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('useremail', models.CharField(max_length=100)),
                ('userpassword', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 7, 31, 13, 50, 28, 536810, tzinfo=utc))),
                ('lastlogin', models.DateTimeField(blank=True, null=True)),
                ('lastlogout', models.DateTimeField(blank=True, null=True)),
                ('logintoken', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
