from django.test import TestCase

from menu.models import Menu
from menu.validators import is_valid_order


class ValidatorsTestCase(TestCase):

    def test__is_valid_checks_with_existing_field_in_model_or_custom_fields(self):
        self.assertTrue(is_valid_order(model=Menu, ordering='name'))
        self.assertTrue(is_valid_order(model=Menu, ordering='dish_count', custom_fields=['dish_count']))

    def test__is_valid_checks_with_not_existing_fields(self):
        self.assertFalse(is_valid_order(model=Menu, ordering='not_existing_field'))
        self.assertFalse(is_valid_order(model=Menu, ordering='not_existing_field', custom_fields=['dish_count']))
