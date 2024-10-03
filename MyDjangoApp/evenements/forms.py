from django import forms
from django.forms import ModelForm
from .models import Venue, Evenement


#Create a the Venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'web', 'email_address')
        labels= {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web_Address'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email_ddress'}),  
        }
        
        
        #Create a the Venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'web', 'email_address')
        labels= {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web_Address'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email_ddress'}),  
        }
        
        
      
        
        
        
#SuperUser EvenementForm
class EvenementFormAdmin(ModelForm):
  class Meta: 
        model = Evenement
        fields = ('name', 'evenement_date', 'venue', 'manager', 'description', 'attendees')
        labels= {
            'name': 'Name',
            'YYYY-MM-DD HH:MM:SS': 'Date',
            'venue': 'Venue',
            'manager': 'Manager',
            'description': 'Description',
            'attendees': 'Attendees',
        }
        
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event_name'}),
            'evenement_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event_date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event_venue'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event_manager'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event_description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'Event_attendees'}),  
        }  
        
        
        
              
#User EvenementForm
class EvenementForm(ModelForm):
  class Meta: 
        model = Evenement
        fields = ('name', 'evenement_date', 'venue', 'description', 'attendees')
        labels= {
            'name': 'Name',
            'YYYY-MM-DD HH:MM:SS': 'Date',
            'venue': 'Venue',
            'description': 'Description',
            'attendees': 'Attendees',
        }
        
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event_name'}),
            'evenement_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event_date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event_venue'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event_description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'Event_attendees'}),  
        }  
    
    

