from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Author, Book, Comment
from .forms import Myform
from django.shortcuts import render, render_to_response
from django.shortcuts import redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def listing(request):
#     book_list = Books.objects.all()
#     paginator = Paginator(contact_list, 2)

#     page = request.GET.get('page')
#     try:
#         books = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         books = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         books = paginator.page(paginator.num_pages)

#     return render(request, 'list.html', {'contacts': contacts})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    context.update(csrf(request))
    return render_to_response("register.html", context)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return redirect("/")
        else:
            # Отображение страницы с ошибкой
            args['errors'] = 'Пользователь не найден!'
            return render_to_response("login.html", args)
    else:
        return render_to_response("login.html", args)


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/")


def item(request, alias):
    context = {}
    buy = False
    try:
        item = Book.objects.get(alias=alias)
    except ObjectDoesNotExist:
        raise Http404
    if request.method == "POST":
        form = Myform(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            form.save()
            return redirect('/book/%s' % alias)
    else:
        form = Myform()
    comments = Comment.objects.all()
    if request.user.is_authenticated():
        buy= True
    context = {
        'buy' : buy,
        'item' : item,
        'form': form,
        'comments' : comments,
        'username' : auth.get_user(request).username,
    }
    return render(request, 'item.html', context)


def home(request):
    books = (
        Book.objects.get(id=18),
        Book.objects.get(id=13),
        Book.objects.get(id=19),
        Book.objects.get(id=16),
        Book.objects.get(id=17),
    )
    context = {
        'books' : books,
        'books_sort' : Book.objects.all().order_by('?')[:3],
        'username' : auth.get_user(request).username,
    }
    return render_to_response('index.html', context)


def author(request, alias):
    try:
        authors = Author.objects.get(alias=alias)
    except:
        raise Http404('not found')
    context = {
        'authors' : authors,
        'username' : auth.get_user(request).username,
    }
    return render_to_response('author.html', context)


def categories_fiction(request):
    books_list = Book.objects.filter(category='fiction').order_by('title')
    paginator = Paginator(books_list, 10)

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)

    context = {
        'books' : books,
        'username' : auth.get_user(request).username,
    }
    return render_to_response('categories.html', context)


def categories_technical(request):
    books_list = Book.objects.filter(category='technical').order_by('title')
    paginator = Paginator(books_list, 10)

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)
    context = {
        'books' : books,
        'username' : auth.get_user(request).username,
    }
    return render_to_response('categories.html', context)


def categories_science(request):
    books_list = Book.objects.filter(category='science').order_by('title')
    paginator = Paginator(books_list, 10)

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)
    context = {
        'books' : books,
        'username' : auth.get_user(request).username,
    }
    return render_to_response('categories.html', context)


def categories_detective(request):
    books_list = Book.objects.filter(category='detective').order_by('title')
    paginator = Paginator(books_list, 10)

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)
    context = {
        'books' : books,
        'username' : auth.get_user(request).username,
    }
    return render_to_response('categories.html', context)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q).order_by('title')
        context = {
            'books' : books,
            'query' : q,
            'username' : auth.get_user(request).username,
        }
        return render_to_response('search.html', context)
    else:
        return HttpResponse('Введите что-нибудь.')

