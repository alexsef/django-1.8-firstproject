# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_author_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='img',
            field=models.CharField(max_length=255, default='a'),
            preserve_default=False,
        ),
    ]
