from api.fixtures import client_vendor_dict
from mobilender.models import Person
from api.fixtures import client_vendor_dict, get_article, get_order, get_person_as_client, get_person_as_vendor, get_site
from api.fixtures import get_client_data_normal
# from api.fixtures import get_client_data_platinum
from django.test import TestCase
from rest_framework.test import APIClient
import json

# Create your tests here.
from unittest.mock import MagicMock, Mock, patch

client = APIClient()

class ApiTestCaseExample(TestCase):
    client = None
    vendor = []
    article = None
    site = None

    def test_create_client(self):
        data = get_person_as_client()
        request = client.post('/api/client/', data, format='json')
        assert request.status_code == 201

    def test_create_vendor(self):
        data = get_person_as_vendor()
        request = client.post('/api/client/', data, format='json')
        assert request.status_code == 201
        
    def test_create_articles(self):
        self.test_create_vendor()
        data = get_article()
        request = client.post('/api/articles/', data, format='json')
        assert request.status_code == 201
       
    def test_create_site(self):
        data = get_site()
        request = client.post('/api/sites/', data, format='json')
        assert request.status_code == 201