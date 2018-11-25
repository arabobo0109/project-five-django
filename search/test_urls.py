from django.urls import resolve
from django.test import TestCase
from .urls import  do_search_products


class TestURLS(TestCase):
    
    # Tests the different URL patterns, and confirms they can be found  
    def test_urlpatterns(self):
        found = resolve('/search/')
        self.assertEqual(found.func, do_search_products)