from django.db import models

# Create your models here.

class Quote(models.Model):
    """ Encapsulate the idea of a quote"""

    # data attribute:
    text = models.TextField(blank=True)
    author = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    def __repr__(self):
        """return a string rep of the object"""
        return '"%s" - %s' % (self.text, self.author)

