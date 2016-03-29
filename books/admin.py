from django.contrib import admin
from .models import Author, Book, Comment


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    exclude = ('pub_date', 'width_field', 'height_field')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'birthday')


class CommentAdmin(admin.ModelAdmin):
    fields = ('text',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)

