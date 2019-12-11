from django import forms
from django.forms import widgets
from .models import Event, Venue, Dance

class CreateEventForm(forms.ModelForm):
    ''' form to add new events to database'''
    #set fields for form submission and provide choices for user to input 
    eventname = forms.CharField(label="Event Name:", required=True)
    venue = forms.ModelChoiceField(label="Venue Name:", required=True, queryset=Venue.objects.all())
    CHOICES = [("12 a.m.", "12 a.m."),("1 a.m.", "1 a.m."),("2 a.m.", "2 a.m."),("3 a.m.", "3 a.m."),("4 a.m.", "4 a.m."),
    ("5 a.m.", "5 a.m."),("6 a.m.", "6 a.m."),("7 a.m.", "7 a.m."),("8 a.m.", "8 a.m."),("9 a.m.", "9 a.m."),("10 a.m.", "10 a.m."),
    ("11 a.m.", "11 a.m."),("12 p.m.", "12 p.m."),("1 p.m.", "1 p.m."),("2 p.m.", "2 p.m."),("3 p.m.", "3 p.m."),
    ("4 p.m.", "4 p.m."),("5 p.m.", "5 p.m."),("6 p.m.", "6 p.m."),("7 p.m.", "7 p.m."),("8 p.m.", "8 p.m."),
    ("9 p.m.", "9 p.m."),("10 p.m.", "10 p.m."),("11 p.m.", "11 p.m."),] #for time field in order to separate date and time into two fields
    date_time = forms.ChoiceField(label="Start Time:", required=False, widget=forms.Select, choices=CHOICES)
    date = forms.DateField(label="Event Date:", required=True, widget=forms.SelectDateWidget(years=range(2019,2020,2021)))
    website = forms.URLField(label="Website:", required=False)
    image = forms.URLField(label="Add Event Image (URL):", required=False)

    class Meta:
        model = Event
        fields = ['eventname', 'venue', 'date_time', 'date', 'website', 'image', 'dances'] #form fields to display from Event model
    #image_url = forms.CharField(label="Profile Photo", required=True)

class CreateVenueForm(forms.ModelForm):
    ''' form to add new venues to the database'''
    #set fields for form submission and provide choices for user to input
    venuename = forms.CharField(label="Venue Name:", required=True,)
    streetname = forms.CharField(label="Address:", required=True)
    city = forms.CharField(label="City:", required=True)
    CHOICES = [("AL","Alabama"),("AK","Alaska"),("AZ","Arizona"),("AR","Arkansas"),("CA","California"),("CO","Colorado"),
    ("CT","Connecticut"),("DE","Delaware"), ("FL","Florida"),("GA","Georgia"),("HE","Hawaii"),("ID","Idaho"),
    ("IL","Illinois"),("IN","Indiana"),("IA","Iowa"),("KS","Kansas"),("KY","Kentucky"),("LA","Louisiana"),("ME","Maine"),
    ("MD","Maryland"),("MA","Massachusetts"),("MI","Michigan"),("MN","Minnesota"),("MS","Mississippi"),("MO","Missouri"),("MT","Montana"),("NE","Nebraska"), 
    ("NV","Nevada"),("NH","New Hampshire"),("NJ","New Jersey"),("NM","New Mexico"),("NY","New York"),("NC","North Carolina"),
    ("ND","North Dakota"),("OH","Ohio"),("OK","Oklahoma"), ("OR","Oregon"),("PA","Pennsylvania"),("RI","Rhode Island"),("SC","South Carolina"),
    ("SD","South Dakota"),("TN","Tennessee"),("TX","Texas"),("UT","Utah"),
    ("VT","Vermont"),("VA","Virginia"),("WA","Washington"),("WV","West Virginia"),("WI","Wisconsin"),("WY","Wyoming")] #for state field
    state = forms.ChoiceField(label="State:", required=True, choices=CHOICES, widget=forms.Select)
    zipcode = forms.CharField(label="Zip Code:", required=False, max_length="5")
    image = forms.URLField(label="Add Image of Venue:", required=False)
    CHOICES = [('Yes','Yes'),('No','No')]
    handicap = forms.ChoiceField(label="Handicap Accessible?", required=False, choices=CHOICES, widget=forms.RadioSelect)
    wifi = forms.ChoiceField(label="Wifi Available?", required=False, choices=CHOICES, widget=forms.RadioSelect)
    coatcheck = forms.ChoiceField(label="Coat Check?", required=False, choices=CHOICES, widget=forms.RadioSelect)
    food = forms.ChoiceField(label="Food Available In Venue?", required=False, choices=CHOICES, widget=forms.RadioSelect)
    CHOICES=[('Free','Free Parking'),
        ('Garage','Parking Garage'), ('None', 
        'No Venue Parking')]
    parkinggarage = forms.ChoiceField(label="Parking Garage Available?", required=False, choices=CHOICES, widget=forms.Select)


    class Meta:
        model = Venue
        fields = ['venuename', 'streetname', 'city', 'state', 
        'zipcode', 'image', 'handicap', 'wifi', 'coatcheck', 'food', 'parkinggarage',] #form fields to display from Venue model

class UpdateEventForm(forms.ModelForm):
    ''' form to update event information in the database'''
    class Meta:
        model = Event
        fields = ['image', 'eventname', 'venue', 'date', 'website', 'dances'] # fields from model that should use when Updating Event information 


class UpdateVenueForm(forms.ModelForm):
    ''' form to update venue information in the database'''
    class Meta:
        model = Venue
        fields = ['venuename', 'streetname', 'city', 'state', 
        'zipcode', 'image', 'handicap', 'wifi', 'coatcheck', 'food', 'parkinggarage',] # fields from model that should use when updating Venue information