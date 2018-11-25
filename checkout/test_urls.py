from django.urls import resolve
from django.test import TestCase
from .urls import checkout


class TestURLS(TestCase):
    
    # Tests the different URL patterns, and confirms they can be found  
    def test_urlpatterns(self):
        found = resolve('/checkout/')
        self.assertEqual(found.func, checkout)