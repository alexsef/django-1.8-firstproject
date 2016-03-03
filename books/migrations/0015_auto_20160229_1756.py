# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20160225_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=255, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'db_table': 'Comments',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(max_length=100, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(verbose_name='Описание автора', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='img',
            field=models.CharField(max_length=255, verbose_name='Ссылка на картинку'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.SlugField(max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Описание книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.CharField(max_length=255, verbose_name='Ссылка на обложку'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=20, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='book',
            name='short_description',
            field=models.CharField(max_length=255, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_link',
            field=models.ForeignKey(to='books.Book'),
        ),
    ]
