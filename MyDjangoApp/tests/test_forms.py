from django.test import TestCase
from evenements.forms import VenueForm
from evenements.models import Venue
from django.contrib.auth.models import User
from datetime import datetime

class TestForms(TestCase):

    
        
        def test_Venue_form_valid_data(self):
            form = VenueForm(data={
                'name': 'Venue',
                'address': 'Address',
                'zip_code': '8000',
                'phone': '28252415',
                'web': 'https://www.google.com',
                'email_address': 'louay.zarrouk@esprit.tn',
            })
            
            self.assertTrue(form.is_valid())
            
        
        
        def test_Venue_form_no_data(self):
            form = VenueForm(data={})
            
            self.assertFalse(form.is_valid())
            self.assertEqual(len(form.errors), 3)
        