from django.core.management.base import BaseCommand
from myapp.models import Book, Author, Genre
from datetime import datetime

class Command(BaseCommand):
    help = 'Creates initial data for the book list application'

    def handle(self, *args, **kwargs):
        self.create_authors()
        self.create_books()

    def create_authors(self):
        author1 = Author(name="F. Scott Fitzgerald", birthdate="1896-09-24", nationality="American")
        author2 = Author(name="Harper Lee", birthdate="1926-04-28", nationality="American")
        author3 = Author(name="George Orwell", birthdate="1903-06-25", nationality="British")
        author4 = Author(name="Jane Austen", birthdate="1775-12-16", nationality="British")
        author5 = Author(name="J.R.R. Tolkien", birthdate="1892-01-03", nationality="British")

        authors = [author1, author2, author3, author4, author5]

        for author in authors:
            author.save()
            self.stdout.write(self.style.SUCCESS(
                'Successfully created authors.'
            ))

    def create_books(self):
    # Retrieve or create the Author instances
        fitzgerald = Author.objects.filter(name="F. Scott Fitzgerald").first()
        # if not fitzgerald:
        #     fitzgerald = Author.objects.create(name="F. Scott Fitzgerald", birthdate="1896-09-24")

        lee = Author.objects.get_or_create(name="Harper Lee", defaults={"birthdate": "1926-04-28"})[0]
        orwell = Author.objects.get_or_create(name="George Orwell", defaults={"birthdate": "1903-06-25"})[0]
        austen = Author.objects.get_or_create(name="Jane Austen", defaults={"birthdate": "1775-12-16"})[0]
        tolkien = Author.objects.get_or_create(name="J.R.R. Tolkien", defaults={"birthdate": "1892-01-03"})[0]

    # Create Book instances
        book1 = Book(title="The Great Gatsby", author=fitzgerald, genre="Fiction",
                 publication_date="1925-04-10", summary="A novel about the American Dream.")
        book2 = Book(title="To Kill a Mockingbird", author=lee, genre="Classics",
                 publication_date="1960-07-11", summary="A story of racial injustice in the American South.")
        book3 = Book(title="1984", author=orwell, genre="Dystopian",
                 publication_date="1949-06-08", summary="A classic novel about totalitarianism.")
        book4 = Book(title="Pride and Prejudice", author=austen, genre="Romance",
                 publication_date="1813-01-28", summary="A romantic novel set in the early 19th century.")
        book5 = Book(title="The Hobbit", author=tolkien, genre="Fantasy",
                 publication_date="1937-09-21", summary="An adventure novel about Bilbo Baggins.")

        books = [book1, book2, book3, book4, book5]

        for book in books:
            book.save()
            self.stdout.write(self.style.SUCCESS('Successfully created books.'))


