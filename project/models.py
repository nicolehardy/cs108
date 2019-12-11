from django.db import models
from django.urls import reverse
# Create your models here.

class Event(models.Model):
    '''Stores information about each event including time, venue (fk) and dances available'''
    eventname = models.TextField()
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE) #takes fk from Venue Model
    date = models.DateField() #model fields to be collected under forms
    date_time = models.TimeField(blank=True)
    website = models.URLField(blank=True)
    image = models.URLField(blank=True)
    dances = models.ManyToManyField('Dance') #MTM field of dances to allow multiple dance selections in Event page
    def showallevents(self):
        '''captures all event objects and sorts them by date'''
        event = Event.objects.all()
        event = event.order_by("-date")

    def get_absolute_url(self):
        '''return url to display newly updated event'''
        return reverse("show_event", kwargs={"pk":self.pk})
    
    def get_venue_info(self):
        '''Obtains venue info for event'''
        venue_info = Venue.objects.filter(id=self.pk)[0]

        return venue_info

    def get_dances(self):
        '''method that returns a QuerySet of dances for individual event'''
        dance = Event.objects.filter(id=self.pk)[0] # gets rid of the query set
        all_dances = dance.dances.all()
        return all_dances

    def __str__(self):
        ''' returns string representation of the Event information to display. '''
        return "%s" % (self.eventname)



class Venue(models.Model):
    '''Stores information about Venue location including photos and amenities available at the location'''
    venuename = models.TextField()
    streetname = models.TextField() #model fields to be collected under forms
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField(blank=True)
    image = models.URLField(blank=False)
    website = models.URLField(blank=True)
    handicap = models.TextField()
    wifi = models.TextField()
    coatcheck = models.TextField()
    food = models.TextField()
    parkinggarage = models.TextField()

    def get_events(self):
        '''Obtains events occurring at this venue'''
        eventlist = Event.objects.filter(id=self.pk) # 
        return eventlist

    def get_absolute_url(self):
        '''return url to display newly updated venue'''
        return reverse("show_venue", kwargs={"pk":self.pk})

    def __str__(self):
        '''returns a string representation of the Venue information to display.'''
        return "%s" % (self.venuename)

class Dance(models.Model):
    '''Stores information about dance name and description along with a video example - foreign key for event model'''
    dance = models.TextField()
    description = models.TextField() #model fields added under ADMIN only
    video = models.URLField()

    def __str__(self):
        ''' returns a string representation of the Dance information to display.'''
        return "%s" % (self.dance)