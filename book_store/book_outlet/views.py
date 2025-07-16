from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Max, Min
from book_outlet.models import Book
from .constants import BOOKS_DETAILS_PAGE


def index(request):
    books = Book.objects.all().order_by('title')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))['rating__avg']

    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_numbers_of_books': num_books,
        'average_rating': avg_rating,
        'detail_page': BOOKS_DETAILS_PAGE
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestseller
    })