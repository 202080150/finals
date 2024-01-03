from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book, Author, Genre
from .forms import AuthorForm, GenreForm, BookForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import json

# Create your views here.
class HomePageView(ListView):
    model = Book
    context_object_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'home'
        return context
    
class BookListView(ListView):
    model = Book
    context_object_name = 'book'
    template_name = 'books.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'book'
        return context
    
class AuthorListView(ListView):
    model = Author
    context_object_name = 'author'
    template_name = 'authors.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'author-list'
        return context
    

class GenreListView(ListView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'genres.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'genre-list'
        return context
    

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_add.html'
    success_url = reverse_lazy('author-list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_edit.html'
    success_url = reverse_lazy('author-list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_del.html'
    success_url = reverse_lazy('author-list')


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre_add.html'
    success_url = reverse_lazy('genre-list')
    

class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre_edit.html'
    success_url = reverse_lazy('genre-list')


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'genre_del.html'
    success_url = reverse_lazy('genre-list')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_add.html'
    success_url = reverse_lazy('book-list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_edit.html'
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_del.html'
    success_url = reverse_lazy('book-list')
