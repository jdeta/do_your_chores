from django.test import TestCase, Client
from django.urls import reverse
from do_your_chores.models import Household, Member


class ChoreBoardViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.board_url = reverse('chores:chores_board')

    def test_board_url_exists(self):
        response = self.client.get(self.board_url)
        self.assertEqual(response.status_code, 200)

    def test_board_template(self):
        response = self.client.get(self.board_url)
        self.assertTemplateUsed(response, 'do_your_chores/chores_board.html')

class NewHouseholdTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.house_url = reverse('chores:new_house')
        self.response = self.client.post(self.house_url, {
            'name': 'Hill House',}, follow=True)

    def test_house_create(self):
        test_house = Household.objects.get(id=1)
        self.assertEquals(test_house.name, 'Hill House')

    def test_new_house_redirect(self):
        self.assertEqual(self.response.redirect_chain[-1][1], 302)
        self.assertEqual(self.response.redirect_chain[-1][0], 'do_your_chores/member_form.html')
