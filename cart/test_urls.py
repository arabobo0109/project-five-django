from django.urls import resolve
from django.test import TestCase
from .urls import view_cart


class TestURLS(TestCase):
    
    # Tests the different URL patterns, and confirms they can be found  
    def test_urlpatterns(self):
        found = resolve('/cart/')
        self.assertEqual(found.func, view_cart)