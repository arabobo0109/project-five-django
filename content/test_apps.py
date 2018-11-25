from django.apps import apps
from django.test import TestCase
from .apps import ContentConfig


class TestContentConfig(TestCase):
    
    def test_app(self):
        self.assertEqual("content", ContentConfig.name)
        self.assertEqual("content", apps.get_app_config("content").name)