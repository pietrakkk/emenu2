from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from menu.tests.factories import MenuFactory


class MenuRestApiTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.menu = MenuFactory()

    def test_get_existing_menu_returns_200(self):
        response = self.client.get(reverse('menu-detail', kwargs={'pk': self.menu.id}), format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], self.menu.id)
        self.assertEquals(response.data['name'], self.menu.name)

    def test_get_not_existing_menu_returns_404(self):
        not_existing_pk = 100
        response = self.client.get(reverse('menu-detail', kwargs={'pk': not_existing_pk}), format='json')

        self.assertEquals(response.status_code, 404)
