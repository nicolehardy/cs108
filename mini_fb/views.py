from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile
# Create your views here.
class ShowAllProfilesView(ListView):
    """ create a subclass of listview to display profiles in a list """
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'showallprofiles'

class ShowProfilePageView(DetailView):
    '''create a subclass of DetailView to display single profile page'''
    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile_page'