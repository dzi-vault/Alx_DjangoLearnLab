from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# BookSerializer converts Book model instances to JSON.
# Includes validation to prevent future publication years.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation: publication_year must not be in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# AuthorSerializer includes nested books.
# It uses the related_name='books' from the ForeignKey.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
