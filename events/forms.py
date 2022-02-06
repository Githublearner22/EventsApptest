from django import forms
from django.forms import ModelForm
from .models import Venue, Event


# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'postcode', 'web','email_address')
        labels = {
        'name':'',
        'address': '',
        'postcode': '',
        'phone': '',
        'web': '',
        'email_address': '',
        }
        widgets = {#adding style
        'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
        'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
        'postcode': forms.TextInput(attrs={'class':'form-control','placeholder':'Postcode'}),
        'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
        'web': forms.TextInput(attrs={'class':'form-control','placeholder':'Website'}),
        'email_address': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'})
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'contact','attendees','description')
        labels = {
        'name':'',
        'event_date': 'YYYY-MM-DD HH:MM:SS', #We can change the time format under widget- Research it
        'venue': 'Venue',
        'contact': 'Contact',
        'attendees': 'Attendees',
        'description': '',
        }
        widgets = {#adding style
        'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
        'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Date'}),
        'venue': forms.Select(attrs={'class':'form-select','placeholder':'Venue'}), #form-select changes to select the venue
        'contact': forms.Select(attrs={'class':'form-select','placeholder':'Contact'}),
        'attendees': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
        'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description'})
        }