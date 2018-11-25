from django.urls import resolve
from django.test import TestCase
from .urls import all_products


class TestURLS(TestCase):
    
    # Tests the different URL patterns, and confirms they can be found  
    def test_urlpatterns(self):
        found = resolve('/products/')
        self.assertEqual(found.func, all_products)