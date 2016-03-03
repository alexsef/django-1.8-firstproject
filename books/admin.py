from django.contrib import admin
from .models import Author, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    fields = (
        'title',
        'author',
        'alias',
        'price',
        'short_description',
        'description',
        'category',
        'image',
        )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'birthday')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)

