# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0033_auto_20160307_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('text', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name_plural': 'Комментарии',
                'db_table': 'Comments',
                'verbose_name': 'Комментарий',
            },
        ),
        migrations.RemoveField(
            model_name='book',
            name='comments_text',
        ),
        migrations.AddField(
            model_name='book',
            name='comment_text',
            field=models.CharField(blank=True, verbose_name='Комментарий', null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, verbose_name='Автор', null=True, to='books.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 20, 37, 29, 744781)),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_link',
            field=models.ForeignKey(to='books.Book', null=True),
        ),
    ]
