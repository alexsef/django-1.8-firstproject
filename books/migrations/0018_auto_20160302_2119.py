# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20160302_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.SlugField(max_length=100, choices=[('fiction', 'художественная'), ('technical', 'техническая'), ('science', 'научная'), ('detective', 'детектив')], verbose_name='Категория'),
        ),
    ]
