from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Genre(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(BaseModel):
    GENRE_CHOICES = (
        ('Fiction', 'Fiction'),
        ('Classics', 'Classics'),
        ('Dystopian', 'Dystopian'),
        ('Romance', 'Romance'),
        ('Fantasy', 'Fantasy'),
        # Add more genres as needed
    )

    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    summary = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title

class BookGenre(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} - {self.genre.name}"
