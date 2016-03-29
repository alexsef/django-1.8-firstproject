# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0027_auto_20160305_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_link',
        ),
        migrations.AddField(
            model_name='book',
            name='comment_text',
            field=models.CharField(verbose_name='Комментарий', null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 17, 4, 29, 195775)),
        ),
    ]
