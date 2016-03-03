# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20160223_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.SlugField(max_length=100),
        ),
    ]
