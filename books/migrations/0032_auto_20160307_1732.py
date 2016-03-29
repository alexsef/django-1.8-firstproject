# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0031_auto_20160307_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='comment_text',
        ),
        migrations.AddField(
            model_name='book',
            name='comments_text',
            field=models.TextField(null=True, blank=True, max_length=255, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 17, 32, 5, 869626)),
        ),
    ]
