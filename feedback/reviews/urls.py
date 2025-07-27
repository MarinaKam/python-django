from django.contrib import admin
from django.urls import path

from . import views
from .constants import STARTING_PAGE, SUBMIT_PAGE, REVIEWS_PAGE, REVIEWS_DETAIL_PAGE

urlpatterns = [
    path("", views.ReviewView.as_view(), name=STARTING_PAGE),
    path("submit", views.SubmitView.as_view(), name=SUBMIT_PAGE),
    path("reviews", views.ReviewList.as_view(), name=REVIEWS_PAGE),
    path("reviews/<int:id>", views.ReviewDetail.as_view(), name=REVIEWS_DETAIL_PAGE),
]
