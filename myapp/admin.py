from django.contrib import admin
from .models import Book, Author, Genre

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "publication_date", "summary")
    search_fields = ("title", "author__name", "genre", "publication_date", "summary")

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "nationality")
    search_fields = ("name", "birthdate", "nationality")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
