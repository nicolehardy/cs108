#pages/ur;s.py

from django.urls import path
from .views import HomePageView, AboutPageView #class def

urlpatterns = [
    # map url in empty string to function homepageview
    #path('', homePageView, name='home') function based view
    path('', HomePageView.as_view(), name='home'), # generic class based view
    path('about/', AboutPageView.as_view(), name='about'), # generic class based view
    
]