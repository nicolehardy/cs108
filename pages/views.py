from django.shortcuts import render

from django.http import HttpResponse #creates a response to url request within this file
# Create your views here.


def homePageView(request):
    """ responds to http request and returns an HttpResponse"""

    s = ''' 
    <html>
    <head>
        <title>Hello, world!</title>
    </head>
    <body>
    <h1>Hello, world!</h1>
    Welcome to our first Django application!
    <p>
    </body>
    </html> 
    '''

    return HttpResponse(s)