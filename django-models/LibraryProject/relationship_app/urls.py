from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import UserLoginView, UserLogoutView, register

urlpatterns = [
    # Task 2 URLs
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Task 3 Authentication URLs
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
