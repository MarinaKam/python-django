from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm

def review(request):
   if request.method == "POST":
      form = ReviewForm(request.POST)

      if form.is_valid():
         form.save()
         return HttpResponseRedirect("/submit")

   else:
      form = ReviewForm()

   return render(request, "reviews/review.html", {
      "form": form,
   })


def submit(request):
   return render(request, "reviews/submit.html")