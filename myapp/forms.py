from django.forms import ModelForm
from django import forms
from .models import Book, Author, Genre

class BookForm(ModelForm):
    publication_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Book
        fields = "__all__"

class AuthorForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Author
        fields = "__all__"

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"
