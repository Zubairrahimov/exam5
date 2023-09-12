from django.urls import path
from .views import (
    AuthorGetView,
    AuthorDeleteView,
    AuthorUpdateView,
    BookDeleteView,
    BookUpdateView,
    BooksGetView,
    AuthorBooksAPIView,
)


urlpatterns =[
    path('authors/', AuthorGetView.as_view()),
    path('author_delete/<int:author_id>', AuthorDeleteView.as_view()),
    path('author_update/', AuthorUpdateView.as_view()),
    path('book_delete/<int:book_id>', BookDeleteView.as_view()),
    path('book_update/', BookUpdateView.as_view()),
    path('books/', BooksGetView.as_view()),
    path("author_books/<int:author_id>", AuthorBooksAPIView.as_view()),
    
]