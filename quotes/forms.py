# quotes/form.py
from django import forms
from .models import Quote

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
