from django.db import models
from django.urls import reverse #obtain url from pattern name

# Create your models here.
class Profile(models.Model): 
    """ stores information for each profile """
    firstname = models.TextField()
    lastname = models.TextField()
    city = models.TextField()
    email = models.TextField()
    image_url = models.URLField()

    def get_status_messages(self):
        '''Obtains status messages for a particular profile '''
        status = StatusMessage.objects.filter(profile=self.pk) # retrieves status message info stored in class StatusMessage
        return status

    def get_absolute_url(self):
        '''return url to display newly added profile''' # return url for django to redirect to using pk 
        return reverse("show_profile_page", kwargs={"pk":self.pk})

    def __str__(self):
        """returns string representation of the profile name """

        return "%s %s" %(self.firstname, self.lastname)

class StatusMessage(models.Model):
    '''models the data attributes of Facebook status message including timestamp, individual message,
    and profile that posted the message. '''
    timestamp = models.DateTimeField(auto_now_add=True) #auto generates time status posted using model class 
    message = models.TextField()
    profile = models.ForeignKey('Profile', on_delete="CASCADE") #links to Profile class using foreignkey

    def __str__(self):
        ''' returns string representation of the status message to display'''
        return "%s posted '%s' at %s" % (self.profile, self.message, self.timestamp)
