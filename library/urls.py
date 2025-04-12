from django.urls import path
from .views import (
    AuthorCreateView, AuthorListView,
    BookCreateView, BookListView,
    BorrowRecordCreateView, BorrowRecordListView,
    ExportExcelView, HomeView
)

urlpatterns = [
    path('authors/add/', AuthorCreateView.as_view(), name='author-add'),
    path('authors/', AuthorListView.as_view(), name='author-list'),

    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/', BookListView.as_view(), name='book-list'),

    path('borrows/add/', BorrowRecordCreateView.as_view(), name='borrow-add'),
    path('borrows/', BorrowRecordListView.as_view(), name='borrow-list'),

    path('export/', ExportExcelView.as_view(), name='export-excel'),

    path('', HomeView.as_view(), name='home'),
]
