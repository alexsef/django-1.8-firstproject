# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20160217_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='alias',
            field=models.SlugField(verbose_name='Alias автора', default='asd'),
            preserve_default=False,
        ),
    ]
