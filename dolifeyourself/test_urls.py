from django.urls import resolve
from django.test import TestCase
from .urls import index

class TestURLS(TestCase):
    
    # Tests the different URL patterns, and confirms they can be found  
    def test_urlpatterns(self):
        found = resolve('/')
        self.assertEqual(found.func, index)