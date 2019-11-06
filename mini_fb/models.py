from django.db import models

# Create your models here.
class Profile(models.Model):
    """ stores information for each profile """
    firstname = models.TextField()
    lastname = models.TextField()
    city = models.TextField()
    email = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        """returns string representation of the object """

        return "%s %s       %s" %(self.firstname, self.lastname, self.city)