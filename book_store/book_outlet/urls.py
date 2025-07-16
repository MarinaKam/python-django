from django.urls import path

from . import views
from .constants import STARTING_PAGE, BOOKS_PAGE, BOOKS_DETAILS_PAGE

urlpatterns = [
    path("", views.index, name=STARTING_PAGE),
    path("<slug:slug>", views.book_detail, name=BOOKS_DETAILS_PAGE)
    # path("<int:book_id>", views.book_detail, name=BOOKS_DETAILS_PAGE)
]