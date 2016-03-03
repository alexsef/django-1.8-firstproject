# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_auto_20160303_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='img',
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='', width_field='width_field', height_field='height_field', verbose_name='Картинка'),
        ),
    ]
