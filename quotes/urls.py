#pages/ur;s.py

from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuotePageView #class def

urlpatterns = [
    # map url in empty string to function homepageview
    
    path('all', HomePageView.as_view(), name='home'), # generic class based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'),
    path('', RandomQuotePageView.as_view(), name='random'),
]