from django.test import TestCase,Client
from django.urls import reverse, resolve
from evenements.models import Evenement, Venue
import json
from django.contrib.auth.models import User

class TestViews(TestCase):
  
    def test_Evenement_list_GET(self):
        client = Client()
        response = client.get(reverse('list-evenements'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'evenements/evenement_list.html')
    
    
    def test_Eveneement_POST(self):
        client = Client()
        Evenement = client.post(reverse('add-evenement'), {
            'name': 'Evenement 1',
            'description': 'Evenement 1 description',
            'date': '2021-01-01',
            'venue': 'Test Venue',
            'manager': 'testuser',
        })
        Evenement = self.client.post(self.detail_url,)
        self.assertEqual(Evenement.status_code, 200)
        
        
    
    
    def Test_Evenement_DELETE(self):
        client = Client()
        Evenement = client.delete(reverse('delete-evenement', args=[1]))
        self.assertEqual(Evenement.status_code, 200)    
        
        
    
        
        
    def setUp(self):
        self.client=Client()
        self.list_url=reverse('list-evenements')
        
        self.detail_url=reverse('show-venue',args=[1])
        
        
        
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.venue = Venue.objects.create(
            name='Test Venue',
            address='123 Test St',
            zip_code='12345',
            phone='123-456-7890',
            web='https://testvenue.com',
            email_address='contact@testvenue.com',
            owner=self.user.id)
        self.show_venue_url = reverse('show-venue', args=[self.venue.id])
        
        
        # Connecte l'utilisateur pour accéder à la vue
        self.client.login(username='testuser', password='12345')
        # Effectue une requête GET sur la vue
        response = self.client.get(self.show_venue_url)
        # Vérifie le statut HTTP de la réponse
        self.assertEqual(response.status_code, 200)
        # Vérifie que le bon template est utilisé
        self.assertTemplateUsed(response, 'evenements/show_venue.html')
        # Vérifie que les informations du lieu sont bien présentes dans le contexte de la réponse
        self.assertContains(response, 'Test Venue')
        self.assertContains(response, '123 Test St')
        self.assertContains(response, 'https://testvenue.com')
        
        
        
        
        