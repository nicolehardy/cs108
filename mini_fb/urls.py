#pages/ur;s.py

from django.urls import path
from .views import ShowAllProfilesView #class def

urlpatterns = [
    # map url in empty string to function homepageview
    
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles') # generic class based view
]