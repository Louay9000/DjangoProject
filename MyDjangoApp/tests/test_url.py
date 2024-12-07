from django.test import SimpleTestCase
from django.urls import reverse, resolve
from evenements.views import all_evenements, add_evenement, update_evenement, delete_evenement 



class TestUrls(SimpleTestCase):
  
      def test_list_url_resolves(self):
        url = reverse('list-evenements')
        print(resolve(url))
        self.assertEqual(resolve(url).func, all_evenements)
        
        
      def test_add_url_resolves(self):
        url = reverse('add-evenement')
        print(resolve(url))
        self.assertEqual(resolve(url).func, add_evenement)
        
        
      def test_update_url_resolves(self):
        url = reverse('update-evenement', args=['evenement_id'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, update_evenement)
      
      
      def test_delete_url_resolves(self):
        url = reverse('delete-evenement', args=['evenement_id'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, delete_evenement)
        
        

      