from django.test import TestCase
from .models import Address, Person
from api.fixtures import get_client_data_normal, client_vendor_dict
# Create your tests here.


class MobilenderTestExamples(TestCase):
    def create_person(self):
        data = client_vendor_dict()
        client = data.get('client')
        return Person.objects.create(**client)
    
    def test_person_created(self):
        person = self.create_person()
        self.assertTrue(isinstance(person,Person))
        self.assertEqual(person.__str__(), f'{person.name}-{person.id}')

    def create_address_person(self):
        data = client_vendor_dict()
        person = self.create_person()
        address = data.get('address')
        address = next(iter(address))
        address['person_id'] = person
        return Address.objects.create(**address)

    def test_address_created(self):
        address = self.create_address_person()
        self.assertTrue(isinstance(address, Address))