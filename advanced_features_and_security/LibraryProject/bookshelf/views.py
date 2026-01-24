from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book
from .forms import ExampleForm

@permission_required("bookshelf.can_view", raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST.get("title"),
            author=request.POST.get("author"),
            published_date=request.POST.get("published_date"),
        )
        return redirect("list_books")
    return render(request, "bookshelf/add_book.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published_date = request.POST.get("published_date")
        book.save()
        return redirect("list_books")
    return render(request, "bookshelf/edit_book.html", {"book": book})

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect("list_books")
# Create your views here.
