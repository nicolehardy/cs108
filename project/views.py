from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Event, Venue, Dance
from .forms import CreateEventForm, CreateVenueForm, UpdateEventForm, UpdateVenueForm
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.

class AddEventView(CreateView):
    ''' Creates a new event object to be added to the database. '''
    
    form_class = CreateEventForm
    template_name = "project/create_event_form.html"
    queryset = Venue.objects.all() #collect venues for use as fk in model

    def get_success_url(self): #redirect after creation
        '''return url to redirect following creation of event'''
        # get pk for event
        #event_pk = self.kwargs['event_pk']
        # reverse show event page
        return reverse('show_event',args=(self.object.id,))

    def form_valid(self, form):
        '''saves input from user to database'''
        form.instance.user = self.request.user
        form.save()
        return super(AddEventView, self).form_valid(form) #used for submission form



class AddVenueView(CreateView):
    ''' Creates a new venue object to be added to the database. '''
    
    form_class = CreateVenueForm
    template_name = "project/create_venue_form.html"

    def form_valid(self, form):
        '''saves input from user to database'''
        form.instance.user = self.request.user
        form.save()
        return super(AddVenueView, self).form_valid(form) #used for submission form

    def get_success_url(self): #redirect after creation
        '''return url to redirect following creation'''
        # get pk for venue
        # venue_pk = self.kwargs['venue.pk']
        # reverse show venue page
        # return reverse('venue_page', kwargs={'pk':venue_pk})
        return reverse('show_venue',args=(self.object.id,))

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


class ShowAllEventsView(ListView): #used for homepage to display all objects in the Event model
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

def add_dance(request, event_pk, dance_pk): 
    '''custom view function that allows friend requests outside admin'''
    event = Event.objects.get(pk=event_pk)
    dance = Dance.objects.get(pk=dance_pk)
    event.dances.add(dance) #links dance primary key to event primary key in a many to many relationship
    return redirect(reverse("show_event_page", kwargs={'pk': event_pk}))

class UpdateVenueView(UpdateView): #takes current venue information, displays it for user to edit and save to database as same venue
    ''' updates venue page using UpdateView class and saves it to the database'''
    form_class = UpdateVenueForm
    template_name = "project/update_venue.html"
    queryset = Venue.objects.all() 

