from django.test import TestCase
from evenements.models import Evenement


class TestModels(TestCase):
    def setUp(self):
        self.evenement = Evenement.objects.create(
            titre='Test Evenement',
            description='Test Description',
            date='2021-12-12',
            heure='12:00',
            lieu='Test Lieu',
            prix='10.00',
            places='100',
        )
        


def test_evenement_is_assigned_slug_on_creation(self):
    self.assertEquals(self.evenement.slug, 'test-evenement')