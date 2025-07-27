from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review


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


class ReviewList(ListView):
   template_name = "reviews/review_list.html"
   model = Review
   context_object_name = "reviews"

   def get_queryset(self):
      base_query = super().get_queryset()
      data = base_query.filter(rating__gte=4)
      return data

class ReviewDetail(DetailView):
   template_name = "reviews/review_item.html"
   model = Review
