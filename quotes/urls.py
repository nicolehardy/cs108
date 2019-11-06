#pages/ur;s.py

from django.urls import path
from .views import HomePageView #class def

urlpatterns = [
    # map url in empty string to function homepageview
    
    path('', HomePageView.as_view(), name='home') # generic class based view
]