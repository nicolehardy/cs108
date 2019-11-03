from django.shortcuts import render
from django.http import HttpResponse #creates a response to url request within this file
from django.views.generic import TemplateView # base class for a generic view
#eate your views here.

class HomePageView(TemplateView):
    ''' Inherit from the generic templateview to yse an external HTML template file.'''
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    ''' Inherit from the generic templateview to yse an external HTML template file.'''
    template_name = 'pages/about.html'

#def homePageView(request):
#    """ responds to http request and returns an HttpResponse"""
#
#    s = ''' 
#    <html>
#    <head>
#        <title>Hello, world!</title>
#    </head>
#    <body>
#    <h1>Hello, world!</h1>
#    Welcome to our first Django application!
#    <p>
#    </body>
#    </html> 
#    '''
#
#    return HttpResponse(s)