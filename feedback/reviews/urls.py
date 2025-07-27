from django.contrib import admin
from django.urls import path

from . import views
from .constants import STARTING_PAGE, SUBMIT_PAGE

urlpatterns = [
    path("", views.review, name=STARTING_PAGE),
    path("submit", views.submit, name=SUBMIT_PAGE),
]
