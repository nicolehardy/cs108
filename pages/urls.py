#pages/ur;s.py

from django.urls import path
from .views import homePageView #response function

urlpatterns = [
    # map url in empty string to function homepageview
    path('', homePageView, name='home')
]