#mini_fb/urls.py

from django.urls import path
from .views import * #class def

urlpatterns = [
    # map url in empty string to function view
    
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'), # generic class based view
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), # detail view class
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/<int:pk>/post_status', create_status_message, name='post_status'), #function definition does not need to call parameters to map URL
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name='delete_status'),
    path('profile/<int:profile_pk>/news_feed', ShowNewsFeedView.as_view(), name='news_field'),
    path('profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name='show_possible_friends'),
    path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', add_friend, name='add_friend'),
    
]