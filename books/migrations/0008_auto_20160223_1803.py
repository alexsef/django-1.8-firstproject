# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_author_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author1',
            new_name='author',
        ),
    ]
