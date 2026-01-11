from bookshelf.models import Book

# RETRIEVE the book we created
book = Book.objects.get(title="1984")
book
# Output:
# <Book: 1984>
