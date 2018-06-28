from django.test import TestCase
from django.test import Client, RequestFactory, TestCase

# Create your tests here.
# Load index page
class GetViewTest(TestCase):
    def setup(self):
        client = Client()

    # Test to make sure the index page loads
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# Summarize some text
