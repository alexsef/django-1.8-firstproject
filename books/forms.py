from django.forms import ModelForm
from .models import Book, Comment

class Myform(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
