from django.test import TestCase
from do_your_chores.models import Household

class HouseholdTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_household = Household.objects.create(name='Hill House')
    
    def test_name_label(self):
        name_label = Household.objects.get(pk=self.test_household.pk)._meta.get_field('name').verbose_name
        self.assertEqual(name_label, 'name')

    def test_name_max_length(self):
        test_house = Household.objects.get(pk=self.obj_id)
        name_length = test_house._meta.get_field('name').max_length
        self.assertEqual(name_length, 32)

    def test_name_string_output(self):
        test_house = Household.objects.get(pk=self.obj_id)
        self.assertEqual(test_house.name, str(test_house.name))

