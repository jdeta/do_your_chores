from django.test import TestCase

class ChoreBoardViewTest(TestCase):

    def test_view_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
