from django import forms
from django.forms import widgets
from .models import Event, Venue

class CreateEventForm(forms.ModelForm):
    ''' form to add new events to database'''

    eventname = forms.CharField(label="Event Name:", required=True)
    venue = forms.CharField(label="Venue Name:", required=True)
    date_time = forms.DateTimeField(label="Start Time:", required=True)
    date = forms.DateField(label="Event Date:", required=True)
    website = forms.URLField(label="Website:", required=False)
    image = forms.ImageField(label="Add Image of Event:", required=False)

    class Meta:
        model = Event
        fields = ['image', 'eventname', 'venue', 'date_time', 'date', 'website',]
    #image_url = forms.CharField(label="Profile Photo", required=True)

class CreateVenueForm(forms.ModelForm):
    ''' form to add new venues to the database'''
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
    ("VT","Vermont"),("VA","Virginia"),("WA","Washington"),("WV","West Virginia"),("WI","Wisconsin"),("WY","Wyoming")]
    state = forms.ChoiceField(label="State:", required=True, choices=CHOICES, widget=forms.Select)
    zipcode = forms.CharField(label="Zip Code:", required=False, max_length="5")
    image = forms.ImageField(label="Add Image of Venue:", required=False)
    CHOICES = [('Yes','Yes'),('N','No')]
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
        'zipcode', 'image', 'handicap', 'wifi', 'coatcheck', 'food', 'parkinggarage',]

class UpdateEventForm(forms.ModelForm):
    ''' form to update event information in the database'''
    class Meta:
        model = Event
        fields = ['image', 'eventname', 'venue', 'date', 'website',] # fields from model that should use