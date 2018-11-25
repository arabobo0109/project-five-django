from django.urls import resolve
from django.test import TestCase
from .urls import  get_posts


class TestURLS(TestCase):
    
    # Tests the different URL patterns, and confirms they can be found  
    def test_urlpatterns(self):
        found = resolve('/posts/')
        self.assertEqual(found.func, get_posts)