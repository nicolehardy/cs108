from django.db import models
from django.urls import reverse
# Create your models here.

class Event(models.Model):
    '''Stores information about each event including time, venue (fk) and dances available'''
    eventname = models.TextField()
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)
    date = models.DateTimeField()
    website = models.URLField(blank=True)
    image = models.URLField(blank=True)
    def get_absolute_url(self):
        '''return url to display newly updated event'''
        return reverse("show_event", kwargs={"pk":self.pk})
    
    def get_venue_info(self):
        '''Obtains venue info for event'''
        venue_info = Venue.objects.filter(venue_page=self.pk)
        return venue_info

    def __str__(self):
        ''' returns string representation of the Event information to display. '''
        return "%s" % (self.eventname)



class Venue(models.Model):
    '''Stores information about Venue location including photos and amenities available at the location'''
    venuename = models.TextField()
    streetname = models.TextField()
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


    def __str__(self):
        '''returns a string representation of the Venue information to display.'''
        return "%s" % (self.venuename)

class Dance(models.Model):
    '''Stores information about dance name and description along with a video example - foreign key for event model'''
    dance = models.TextField()
    description = models.TextField()
    video = models.URLField()

    def __str__(self):
        ''' returns a string representation of the Dance information to display.'''
        return "%s" % (self.dance)