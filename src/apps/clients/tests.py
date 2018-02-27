from datetime import date
from django.test import TestCase

from apps.clients.models import Client


class ClientTests(TestCase):
    """
    Client model tests
    """
    def setUp(self):
        self.client = Client(first_name='John', last_name='Connor', birth_date=date(1990, 9, 15))

    def test_str(self):
        """
        Test 'str' method
        :return:
        """
        self.assertEquals(str(self.client), 'John Connor')

    def test_full_name(self):
        """
        Test getting client's full name
        :return:
        """
        self.assertEquals(self.client.get_full_name(), 'John Connor')

# TODO: write tests for APIs
