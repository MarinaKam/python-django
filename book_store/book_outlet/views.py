from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404

from book_outlet.models import Book
from .constants import BOOKS_DETAILS_PAGE


def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'detail_page': BOOKS_DETAILS_PAGE
    })

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestseller
    })