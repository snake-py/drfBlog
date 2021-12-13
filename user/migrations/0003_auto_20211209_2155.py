# Generated by Django 3.2.9 on 2021-12-09 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_author_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2021, 12, 9, 21, 55, 42, 324647)),
            preserve_default=False,
        ),
    ]
