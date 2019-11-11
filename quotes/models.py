from django.db import models
import random

# Create your models here.
class Person(models.Model):
    ''' Encapsulates the concept of a person who said the quote'''
    name = models.TextField(blank=False)
    def __str__(self):
        '''reurn a string rep of the person'''
        return self.name
    
     #get image
    def get_random_image(self):
        '''return image of person'''
        #get all images
        images = Image.objects.filter(person=self.pk)
        # pick on at random
        i = random.randint(0, len(images) - 1)

        return images[i]

    def get_all_images(self):
        '''return queryset of all images for one person'''
        #get all images
        #images = Image.objects.filter(person=self.pk)
        images = Image.objects.filter(person=self.pk)
        return images
    

    def get_all_quotes(self):
        '''return queryset of all images for one person'''
        #get all images
        quotes = Quote.objects.filter(person=self.pk)
        return quotes


class Quote(models.Model):
    """ Encapsulates the idea of a quote"""

    # data attribute:
    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete="CASCADE")
    

    def __str__(self):
        """return a string rep of the object"""
        return '"%s" - %s' % (self.text, self.person.name)

   


class Image(models.Model):
    '''Represent an image associate with a person'''
    image_url = models.URLField(blank=True)
    person = models.ForeignKey('Person', on_delete="CASCADE")
    
    def __str__(self):
        """return a string rep of the object"""
        return self.image_url

