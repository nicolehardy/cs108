from django.shortcuts import render

from django.http import HttpResponse #creates a response to url request within this file
# Create your views here.


def homePageView(request):
    """ responds to http request and returns an HttpResponse"""

    return HttpResponse("Hello, world!")