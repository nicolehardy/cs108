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
    friends = models.ManyToManyField("self")

    def get_status_messages(self):
        '''Obtains status messages for a particular profile '''
        status = StatusMessage.objects.filter(profile=self.pk) # retrieves status message info stored in class StatusMessage
        return status

    def get_absolute_url(self):
        '''return url to display newly added profile''' # return url for django to redirect to using pk 
        return reverse("show_profile_page", kwargs={"pk":self.pk})

    def get_friends(self):
        '''method that returns a QuerySet of Friends for individual profile'''
        #friend = Profile.objects.filter(profile=self.pk)
        #return Profile.objects.filter(friends__excludes=self.pk)
        friend = Profile.objects.filter(id=self.pk)[0] # gets rid of the query set
        all_friends = friend.friends.all()
        return all_friends

    def get_news_feed(self):
        '''method that obtains and returns news feed items'''
        news = StatusMessage.objects.all().order_by("-timestamp")
        return news


    def __str__(self):
        """returns string representation of the profile name """

        return "%s %s" %(self.firstname, self.lastname)

class StatusMessage(models.Model):
    '''models the data attributes of Facebook status message including timestamp, individual message,
    and profile that posted the message. '''
    timestamp = models.DateTimeField(auto_now_add=True) #auto generates time status posted using model class 
    message = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE) #links to Profile class using foreignkey
    image = models.ImageField(blank=True)   # actual image  
    # def __str__(self):
    #     """return a string rep of the object"""
    #     if self.image_url:
    #         return self.image_url
    #     else:
    #         return self.image_file.url # url to the image file

    def __str__(self):
        ''' returns string representation of the status message to display'''
        return "%s posted '%s' at %s" % (self.profile, self.message, self.timestamp)
