from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from menu.tests.factories import MenuFactory, DishFactory


class MenuViewsApiTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.menu = MenuFactory()
        self.menu.dishes.add(DishFactory())
        self.menu.dishes.add(DishFactory())

    def test_get_existing_menu_details_returns_valid_html_and_data(self):
        response = self.client.get(reverse('menu-detail-view', kwargs={'pk': self.menu.id}))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context_data['object'].name, self.menu.name)
        self.assertTrue('menu-details.html' in response.template_name)

    def test_get_existing_menu_list_returns_valid_html_and_data(self):
        menu2 = MenuFactory()
        menu2.dishes.add(DishFactory())
        menu2.dishes.add(DishFactory())

        response = self.client.get(reverse('menu-list'))

        self.assertEquals(response.status_code, 200)
        self.assertTrue('menu-list.html' in response.template_name)
        self.assertEquals(len(response.context_data['object_list']), 2)

    def test_get_not_existing_menu_returns_404(self):
        not_existing_pk = 100
        response = self.client.get(reverse('menu-detail', kwargs={'pk': not_existing_pk}), format='json')

        self.assertEquals(response.status_code, 404)
