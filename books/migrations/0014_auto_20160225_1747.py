# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20160225_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
    ]
