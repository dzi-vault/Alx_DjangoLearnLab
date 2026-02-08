from django.db import models

# Author model represents a writer.
# One Author can have many Books.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model represents a book written by an Author.
# The ForeignKey creates a one-to-many relationship:
# One Author -> Many Books
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'   # allows nested serializer access
    )

    def __str__(self):
        return self.title
# Create your models here.
