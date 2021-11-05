from django.test import TestCase
from do_your_chores.models import Household

class HouseholdTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.obj_id = Household.objects.create(name='Hill House').pk
    
    def test_name_label(self):
        test_house = Household.objects.get(pk=self.obj_id)
        name_label = test_house._meta.get_field('name').verbose_name
        self.assertEqual(name_label, 'name')

    def test_name_max_length(self):
        test_house = Household.objects.get(pk=self.obj_id)
        name_length = test_house._meta.get_field('name').max_length
        self.assertEqual(name_length, 32)



