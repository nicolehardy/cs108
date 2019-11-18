from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Profile, StatusMessage
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def create_status_message(request, pk):
    '''Process a form submission to post a new status message.'''
    # find the profile that matches the `pk` in the URL
    profile = Profile.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']
        
        # save the new status message object to the database
        # if message:

        #     sm = StatusMessage()
        #     #sm.timestamp = timestamp
        #     sm.profile = profile
        #     sm.message = message
        #     sm.save()
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

    # check if form is valid
        if form.is_valid():
            image = form.save(commit=False) # creates but doesnt save yet
            image.profile = profile
            image.message = message
            image.save()

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))

class ShowAllProfilesView(ListView):
    """ create a subclass of listview to display profiles in a list """
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'showallprofiles'

class ShowProfilePageView(DetailView):
    '''create a subclass of DetailView to display single profile page'''
    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile_page'

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    ''' creates a new profile to be added to the database'''
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView): #takes current profile information, displays it for user to edit and save to database as same profile
    ''' updates profile page using UpdateView class and saves it to the database'''
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"
    queryset = Profile.objects.all() 