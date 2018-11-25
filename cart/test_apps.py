from django.apps import apps
from django.test import TestCase
from .apps import CartConfig


class TestCartConfig(TestCase):
    
    def test_app(self):
        self.assertEqual("cart", CartConfig.name)
        self.assertEqual("cart", apps.get_app_config("cart").name)