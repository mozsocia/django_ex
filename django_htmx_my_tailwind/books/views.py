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


#  htmx partials render functions
def book_add_form_hx(request, pk):
    form = BookForm()
    context = {
        "form": form,
        'author_pk': pk
    }

    return render(request, "partials/book_add_form_hx.html", context)


def book_detail_hx(request, pk):
    book = Book.objects.get(id=pk)
    context = {
        "book": book
    }
    # return HttpResponse("owow")
    return render(request, "partials/book_detail_hx.html", context)


def book_update_hx(request, pk):

    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            book = form.save()
            return redirect("book_detail_hx", pk=book.id)

    context = {
        "form": form,
        "book": book,
        # "pk": pk,
    }
    return render(request, "partials/book_update_form_hx.html", context)


def book_delete_hx(request, pk):
    book = get_object_or_404(Book, id=pk)
    book.delete()
    return HttpResponse('')


def book_create_hx(request, pk):
    author = Author.objects.get(pk=pk)
    form = BookForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()

            return redirect("book_detail_hx", pk=book.id)

    return render(request, 'partials/book_add_form_hx.html', {
        "form": form,
        "author_pk": pk
    })


def book_add_cancel_hx(request):
    return HttpResponse('')


def index(request):
    return redirect('author_list')


urlpatterns = [
    path('', index, name='index'),

    path('authors/', author_list, name='author_list'),
    path('author/<pk>/book-list/', author_book_list, name='author_book_list'),

    path('hx/author/<pk>/book_form/', book_add_form_hx, name='book_add_form_hx'),
    path('hx/author/<pk>/book_create/', book_create_hx, name='book_create_hx'),

    path('hx/book/cancel/', book_add_cancel_hx, name='book_add_cancel_hx'),
    path('hx/book/<pk>/detail', book_detail_hx, name="book_detail_hx"),
    path('hx/book/<pk>/delete/', book_delete_hx, name="book_delete_hx"),
    path('hx/book/<pk>/update/', book_update_hx, name="book_update_hx"),



]
