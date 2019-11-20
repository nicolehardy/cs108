# mini_fb/forms.py

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    ''' form to add new profiles to database'''
    #first_name = forms.CharField(label="First Name", required=True)
    #last_name = forms.CharField(label="Last Name", required=True)
    city = forms.CharField(label="Hometown", required=True)
    email = forms.CharField(label="Email", required=True)
    image_url = forms.CharField(label="Profile Photo", required=True)

    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'city', 'email','image_url'] # fields from model that should use

class UpdateProfileForm(forms.ModelForm):
    ''' form to update profile to database'''
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'city', 'email','image_url'] # fields from model that should use

class CreateStatusMessageForm(forms.ModelForm):
    ''' form to add new status to profile'''
    image = forms.ImageField(label="Add Image", required=False)
    class Meta:
        model = StatusMessage
        fields = ['message', "image",] # fields from model that should use