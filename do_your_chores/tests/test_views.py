import datetime

from django.test import TestCase, Client
from django.urls import reverse
from do_your_chores.models import Household, Member, Week, Day


class ChoreBoardViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.board_url = reverse('chores:chores_board')
        self.test_week = Week.objects.create()
        self.today = datetime.date.today().isoweekday()
        self.test_day = Day.objects.create(day=self.today, week=self.test_week)
        self.response = self.client.get(self.board_url)

    def test_board_url_exists(self):
        self.assertEqual(self.response.status_code, 200)

    def test_board_template(self):
        self.assertTemplateUsed(self.response, 'do_your_chores/chores_board.html')


class NewHouseholdTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.house_url = reverse('chores:new_house')
        self.response = self.client.post(self.house_url, {
            'name': 'Hill House',}, follow=True)

    def test_house_create(self):
        test_house = Household.objects.get(name='Hill House')
        self.assertEquals(test_house.name, 'Hill House')

    def test_new_house_redirect(self):
        self.assertEqual(self.response.redirect_chain[-1][1], 302)
        self.assertEqual(self.response.redirect_chain[-1][0], '/member/new')

    def test_new_household_url(self):
        self.assertEqual(self.house_url, '/house/new')


class NewTaskTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.task_url = reverse('chores:new_task')
        self.response = self.client.post(self.task_url, {
            'name':'sweep',
            'day':1,
            'frequency':1,
            }, follow=True)

    def test_new_task_redirect(self):
        self.assertRedirects(self.response, '/task/1', 302)
        self.assertEqual(self.response.redirect_chain[-1][-1], 302)
        self.assertEqual(self.response.redirect_chain[-1][0], '/task/1')


class NewMemberTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.new_member_url = reverse('chores:new_member')
        self.response = self.client.get(self.new_member_url)

    def test_new_member_url(self):
        self.assertEqual(self.new_member_url, '/member/new')

    def test_new_member_view_exists(self):
        self.assertEqual(self.response.status_code, 200)


class HouseHoldDetailTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_house_id = Household.objects.create(name='Hill House').pk
        self.house_detail_url = reverse('chores:household_detail', args=[self.test_house_id])
        self.response = self.client.get(self.house_detail_url)

    def test_household_detail_url(self):
        self.assertEqual(self.house_detail_url, '/house/1')

    def test_household_detail_view_exists(self):
        self.assertEqual(self.response.status_code, 200)



