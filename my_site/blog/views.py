from datetime import date

from django.shortcuts import render
from .models import Post

def get_date(post):
  return post['date']


def starting_page(request):
  latest_posts = Post.objects.all().order_by("-date")[:3]

  return render(request, "blog/index.html", {
    "posts": latest_posts
  })

def posts(request):
  all_posts = Post.objects.all().order_by("-date")

  return render(request, "blog/all-posts.html", {
    "all_posts": all_posts
  })


def post_detail(request, slug):
  post_item = Post.objects.get(slug=slug)

  return render(request, "blog/post-detail.html", {
    "post": post_item
  })