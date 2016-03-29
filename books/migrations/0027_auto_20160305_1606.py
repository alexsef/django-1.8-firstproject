# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0026_auto_20160305_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 5, 16, 6, 50, 5807)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_link',
            field=models.ForeignKey(null=True, to='books.Book'),
        ),
    ]
