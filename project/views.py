from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Event, Venue, Dance
from .forms import CreateEventForm, CreateVenueForm, UpdateEventForm
# Create your views here.

class HomePageView(ListView):
    ''' Inherit from the generic templateview to use an external HTML template file.'''
   
    template_name = 'project/home.html'


class AddEventView(CreateView):
    ''' Creates a new event object to be added to the database. '''
    
    form_class = CreateEventForm
    template_name = "project/create_event_form.html"

class AddVenueView(CreateView):
    ''' Creates a new venue object to be added to the database. '''
    
    form_class = CreateVenueForm
    template_name = "project/create_venue_form.html"


class ShowEventView(DetailView):
    '''create a subclass of DetailView to display single event page'''

    model = Event
    template_name = 'project/show_event_page.html'
    context_object_name = 'event_page'

class ShowVenueView(DetailView):
    '''create a subclass of DetailView to display single venue page'''
    
    model = Venue
    template_name = 'project/show_venue_page.html'
    context_object_name = 'venue_page'


class ShowAllEventsView(ListView):
    """ create a subclass of listview to display all events in a list """
    model = Event
    template_name = 'project/show_all_events.html'
    context_object_name = 'showevents'

class UpdateEventView(UpdateView): #takes current event information, displays it for user to edit and save to database as same event
    ''' updates event page using UpdateView class and saves it to the database'''
    form_class = UpdateEventForm
    template_name = "project/update_event.html"
    queryset = Event.objects.all() 

class ShowDanceView(DetailView):
    ''' creates a subclass of DetailView to display information regarding dances at events'''
    model = Dance
    context_object_name = "dance"