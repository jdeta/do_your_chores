from django.test import TestCase
from django.urls import reverse
from do_your_chores.models import Household


class ChoreBoardViewTest(TestCase):

    def test_board_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class NewMemberViewTest(TestCase):

    def test_new_member_url_exists(self):
        response = self.client.get('/member/new')
        self.assertEqual(response.status_code, 200)

class NewChoreViewTests(TestCase):

    def test_new_chore_url_exists(self):
        response = self.client.get('/chore/new')
        self.assertEqual(response.status_code, 200)
