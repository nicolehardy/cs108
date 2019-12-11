#pages/ur;s.py

from django.urls import path
from .views import * #class def

urlpatterns = [
    # map url in empty string to function homepageview
    
    path('create_venue', AddVenueView.as_view(), name='create_venue'),
    path('create_event', AddEventView.as_view(), name='create_event'),
    path('event/<int:pk>', ShowEventView.as_view(), name='show_event'),
    path('venue/<int:pk>', ShowVenueView.as_view(), name='show_venue'),
    path('event_list', ShowAllEventsView.as_view(), name='show_events'),
    path('event/<int:pk>/update', UpdateEventView.as_view(), name='update_event'),
    path('venue/<int:pk>/update', UpdateVenueView.as_view(), name='update_venue'),
]