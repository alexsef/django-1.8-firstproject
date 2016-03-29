# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0030_auto_20160307_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 17, 15, 35, 410898)),
        ),
    ]
