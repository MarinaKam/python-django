from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review
from .constants import REVIEWS_DETAIL_PAGE


class ReviewView(View):
   def get(self, request):
      form = ReviewForm()

      return render(request, "reviews/review.html", {
         "form": form,
      })

   def post(self, request):
      form = ReviewForm(request.POST)

      if form.is_valid():
         form.save()
         return HttpResponseRedirect("/submit")

      return render(request, "reviews/review.html", {
         "form": form,
      })

class SubmitView(TemplateView):
   template_name = "reviews/submit.html"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["message"] = "This was a success!"
      return context


class ReviewList(TemplateView):
   template_name = "reviews/review_list.html"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      reviews = Review.objects.all()
      context["reviews"] = reviews
      return context


class ReviewDetail(TemplateView):
   template_name = "reviews/review_item.html"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      review_id = kwargs["id"]
      selected_review = Review.objects.get(id=review_id)
      context["review"] = selected_review
      return context
