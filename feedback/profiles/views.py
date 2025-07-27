from django.views.generic import CreateView, ListView

from .models import UserProfile

# Create your views here.

def store_file(file):
    with open("temp/"+file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

class CreateProfileView(CreateView):
    template_name = "profiles/index.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"
