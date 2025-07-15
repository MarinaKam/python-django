from django.urls import path

from . import views
from .constants import STARTING_PAGE, POSTS_PAGE, POSTS_DETAILS_PAGE

urlpatterns = [
    path("", views.starting_page, name=STARTING_PAGE),
    path("posts", views.posts, name=POSTS_PAGE),
    path("posts/<slug:slug>", views.post_detail, name=POSTS_DETAILS_PAGE)
]