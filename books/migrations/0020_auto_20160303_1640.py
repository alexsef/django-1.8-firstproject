# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_auto_20160303_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='i',
            new_name='image',
        ),
    ]
