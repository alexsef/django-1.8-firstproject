from django.db import models
from datetime import datetime

class Author(models.Model):
    class Meta:
        db_table = 'Авторы'
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    author_name = models.CharField(max_length=100, verbose_name='Автор')
    birthday = models.DateField(verbose_name='Дата рождения')
    alias = models.SlugField(verbose_name='Alias автора')
    img = models.CharField(max_length=255, verbose_name='Ссылка на картинку')
    description = models.TextField(blank=True, null=True, verbose_name='Описание автора')

    def __str__(self):
        return '%s' % (self.author_name)


category_ch = (
    ('fiction', 'художественная'),
    ('technical', 'техническая'),
    ('science', 'научная'),
    ('detective', 'детектив'),
)


class Book(models.Model):
    class Meta:
        db_table = 'Книги'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.ForeignKey(Author, verbose_name='Автор', null=True, blank=True)
    alias = models.SlugField(verbose_name='Alias товара')
    pub_date = models.DateTimeField(default=datetime.now())
    price = models.CharField(max_length=20, verbose_name='Цена')
    short_description = models.CharField(max_length=255, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание книги')
    category = models.SlugField(max_length=100, verbose_name='Категория', choices=category_ch)
    image = models.ImageField(width_field='width_field',
                              height_field='height_field',
                              verbose_name='Обложка')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    comment_text = models.CharField(max_length=255, verbose_name='Комментарий',
                                    blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.author, self.title)


class Comment(models.Model):
    class Meta:
        db_table = 'Comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    text = models.TextField(verbose_name='Комментарий')
    comment_link = models.ForeignKey(Book, null=True)

    def __str__(self):
        return '%s' % (self.text)