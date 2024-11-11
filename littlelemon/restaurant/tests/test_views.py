from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setup(self):

        Menu.objects.create(Title="Pizza", Price=100, Inventory=50)
        Menu.objects.create(Title="Burger", Price=50, Inventory=30)
    
    def test_get_all(self):
        client = APIClient()
        response = client.get(reverse('menu-list'))

        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 2)

        if len(response.data) >= 2:
            self.assertEqual(response.data[0]['title'], 'Pizza')
            self.assertEqual(response.data[1]['title'], 'Burger')