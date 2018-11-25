from django.urls import resolve
from django.test import TestCase
from .urls import get_content


class TestURLS(TestCase):
    
    # Tests the different URL patterns, and confirms they can be found  
    def test_urlpatterns(self):
        found = resolve('/content/')
        self.assertEqual(found.func, get_content)