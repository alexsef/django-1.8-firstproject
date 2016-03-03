from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
# from django.template.loader import render_to_string
from .models import Author, Book
from .forms import Myform
from django.shortcuts import render, render_to_response


def home(request):
    books = (
        Book.objects.get(id=18),
        Book.objects.get(id=13),
        Book.objects.get(id=19),
        Book.objects.get(id=16),
        Book.objects.get(id=17),
    )
    books_sort = Book.objects.all().order_by('?')[:3]
    context = {
        'books' : books,
        'books_sort' : books_sort,
    }
    return render_to_response('index.html', context)


def item(request, alias):
    try:
        item = Book.objects.get(alias=alias)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        'item' : item,
    }
    return render_to_response('item.html', context)


def recently(request):
    auth = Author.objects.all()
    books_re = Book.objects.order_by('-pub_date')
    context = {
        'books_re' : books_re,
        'auth' : auth,
    }
    return render_to_response('recently.html', context)


def author(request, alias):
    try:
        authors = Author.objects.get(alias=alias)
    except:
        raise Http404('not found')
    context = {
        'authors' : authors,
    }
    return render_to_response('author.html', context)


def categories_fiction(request):
    books = Book.objects.filter(category='fiction').order_by('title')
    context = {
        'books' : books,
    }
    return render_to_response('categories.html', context)


def categories_technical(request):
    books = Book.objects.filter(category='technical').order_by('title')
    context = {
        'books' : books,
    }
    return render_to_response('categories.html', context)


def categories_science(request):
    books = Book.objects.filter(category='science').order_by('title')
    context = {
        'books' : books,
    }
    return render_to_response('categories.html', context)


def categories_detective(request):
    books = Book.objects.filter(category='detective').order_by('title')
    context = {
        'books' : books,
    }
    return render_to_response('categories.html', context)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        context = {
            'books' : books,
            'query' : q,
        }
        return render_to_response('search.html', context)
    else:
        return HttpResponse('Введите что-нибудь.')

