from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile
# Create your views here.
class ShowAllProfilesView(ListView):
    model = Profile
    template_name = 'templates/show_all_profiles.html'
    context_object_name = 'profile_list'