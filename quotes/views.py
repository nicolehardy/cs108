from django.shortcuts import render
import random
from django.views.generic.edit import CreateView, UpdateView
from .models import Quote, Person
from .forms import CreateQuoteForm, UpdateQuoteForm
# Create your views here.

from django.views.generic import ListView, DetailView

class HomePageView(ListView):
    """ create a subclass of listview to display all quotes"""

    model = Quote
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list'

class QuotePageView(DetailView):
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

    def get_object(self):
        '''return a randomly selected object from Quote '''
        # get all quotes
        all_quotes = Quote.objects.all()
        # pick one at random
        r = random.randint(0, len(all_quotes)-1)
        q = all_quotes[r]
        return q

class PersonPageView(DetailView):
    '''Shows all quotes and images for a person'''
    model = Person
    template_name = 'quotes/person.html'
    context_object_name = 'person'

class CreateQuoteView(CreateView):
    ''' creates new quote and saves it to the database'''
    form_class = CreateQuoteForm
    template_name = "quotes/create_quote.html"
class UpdateQuoteView(UpdateView):
    ''' update quote and saves it to the database'''
    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote.html"
    queryset = Quote.objects.all()

