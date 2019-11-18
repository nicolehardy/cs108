from django.shortcuts import render
import random
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Quote, Person
from .forms import CreateQuoteForm, UpdateQuoteForm, AddImageForm
from django.urls import reverse 
from django.shortcuts import redirect
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
    #context_object_name = 'person'
    def get_context_data(self, **kwargs):
        ''' return dictionary with context data for template to use'''
        context = super(PersonPageView, self).get_context_data(**kwargs)
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form
        return context

class CreateQuoteView(CreateView):
    ''' creates new quote and saves it to the database'''
    form_class = CreateQuoteForm
    template_name = "quotes/create_quote.html"
class UpdateQuoteView(UpdateView):
    ''' update quote and saves it to the database'''
    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote.html"
    queryset = Quote.objects.all()

class DeleteQuoteView(DeleteView):
    ''' Delete quote from the database'''
    template_name = "quotes/delete_quote.html"
    queryset = Quote.objects.all()
    
    def get_success_url(self): #redirect after delete
        '''return url to redirect following deletion of quote'''
        # get pk for quote
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first()
        # find person of quote
        person = quote.person
        # reverse show person page
        return reverse('person', kwargs={'pk':person.pk})

# handle submission of an image
def add_image(request, pk):
    '''custom view function to handle submission of an image upload'''
    # find person object
    person = Person.objects.get(pk=pk)

    # read out data into form
    form = AddImageForm(request.POST or None, request.FILES or None)

    # check if form is valid
    if form.is_valid():
        image = form.save(commit=False) # creates but doesnt save yet
        image.person = person
        image.save()

    else:
        print("Error: the form was not valid.")
    # redirect response with person at URL
    url = reverse('person', kwargs={'pk':pk})
    return redirect(url)