from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review

class ReviewView(CreateView):
   model = Review
   form_class = ReviewForm
   template_name = "reviews/review.html"
   success_url = "/submit"


class SubmitView(TemplateView):
   template_name = "reviews/submit.html"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["message"] = "This was a success!"
      return context


class ReviewList(ListView):
   template_name = "reviews/review_list.html"
   model = Review
   context_object_name = "reviews"

   def get_queryset(self):
      base_query = super().get_queryset()
      data = base_query.filter(rating__gte=1).order_by(
         "-rating"
      )
      return data

class ReviewDetail(DetailView):
   template_name = "reviews/review_item.html"
   model = Review

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      loaded_review = self.object
      request = self.request
      fav_id = request.session.get("fav_review")
      context["is_favorite"] = fav_id == str(loaded_review.id)

      return context

class AddFavorite(View):
   def post(self, request, *args, **kwargs):
      review_id = request.POST.get("review_id")
      request.session["fav_review"] = review_id

      return HttpResponseRedirect("/reviews/" + review_id)
