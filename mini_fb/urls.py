#mini_fb/urls.py

from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView, CreateProfileView, UpdateProfileView, create_status_message #class def

urlpatterns = [
    # map url in empty string to function view
    
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'), # generic class based view
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), # detail view class
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/<int:pk>/post_status', create_status_message, name='post_status'), #function definition does not need to call parameters to map URL
]