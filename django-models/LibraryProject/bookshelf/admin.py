from django.contrib import admin
from .models import Book

# Customize admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns displayed in the list view
    search_fields = ('title', 'author')                     # Fields searchable in admin
    list_filter = ('publication_year',)                    # Filter sidebar for publication year

# Register the Book model with the custom admin settings
admin.site.register(Book, BookAdmin)

# Register your models here.
