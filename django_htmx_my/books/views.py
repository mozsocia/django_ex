from django.http.response import HttpResponse
from django.urls import path
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *

# Create your views here.


def author_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author_list.html', context)


def author_book_list(request, pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author)
    context = {

        "author": author,
        "books": books,
    }

    return render(request, 'author_book_list.html', context)


def book_form_hx(request, pk):
    form = BookForm()
    context = {
        "form": form,
        'pk': pk
    }

    return render(request, "partials/book_form.html", context)


def detail_book_hx(request, pk):
    book = get_object_or_404(Book, id=pk)
    context = {
        "book": book
    }
    return render(request, "partials/book_detail.html", context)


def update_book_hx(request, pk):

    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            book = form.save()
            return redirect("detail_book_hx", pk=book.id)

    context = {
        "form": form,
        "book": book,
        "pk": pk,
    }
    return render(request, "partials/book_form.html", context)


def delete_book_hx(request, pk):
    book = get_object_or_404(Book, id=pk)
    book.delete()
    return HttpResponse('')


def book_create_hx(request, pk):
    author = Author.objects.get(pk=pk)
    form = BookForm(request.POST or None)
    books = Book.objects.filter(author=author)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("detail_book_hx", pk=book.id)
        else:
            return render(request, 'partials/book_form.html', {
                "form": form
            })


urlpatterns = [
    path('', author_list, name='author_list'),
    path('author_book_list/<pk>/', author_book_list, name='author_book_list'),


    path('htmx/book_form/<pk>/', book_form_hx, name='book_form_hx'),
    path('htmx/book_create/<pk>/', book_create_hx, name='book_create_hx'),

    path('htmx/book/<pk>/', detail_book_hx, name="detail_book_hx"),
    path('htmx/book/<pk>/delete/', delete_book_hx, name="delete_book_hx"),
    path('htmx/book/<pk>/update', update_book_hx, name="update_book_hx"),


]
