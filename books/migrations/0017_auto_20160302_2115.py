# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20160301_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, upload_to='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.SlugField(max_length=100, verbose_name='Категория', choices=[('художественная', 'fiction'), ('техническая', 'technical'), ('научная', 'science'), ('детектив', 'detective')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Комментарий'),
        ),
    ]
