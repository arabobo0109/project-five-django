from django.apps import apps
from django.test import TestCase
from .apps import EcommerceConfig


class TestEcommerceConfig(TestCase):
    
    def test_app(self):
        self.assertEqual("ecommerce", EcommerceConfig.name)
        self.assertEqual("ecommerce", apps.get_app_config("ecommerce").name)