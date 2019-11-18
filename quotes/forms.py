# quotes/form.py
from django import forms
from .models import Quote, Image

class CreateQuoteForm(forms.ModelForm):
    ''' form to add new quotes to database'''

    class Meta:
        model = Quote
        fields = ['person', 'text',] # fields from model that should use

class UpdateQuoteForm(forms.ModelForm):
    ''' form to update quote to database'''
    class Meta:
        model = Quote
        fields = ['person', 'text']

class AddImageForm(forms.ModelForm):
    '''A form to collect an image from the user'''
    class Meta:
        model = Image
        fields = ["image_file",]