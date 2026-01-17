# Django CRUD Operations for Book Model

## CREATE
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# Output:
# <Book: 1984>

## RETRIEVE
Book.objects.all()
# Output:
# <QuerySet [<Book: 1984>]>

## UPDATE
book.title = "Nineteen Eighty-Four"
book.save()
book
# Output:
# <Book: Nineteen Eighty-Four>

## DELETE
book.delete()
Book.objects.all()
# Output:
# <QuerySet []>
