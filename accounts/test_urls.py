from django.urls import resolve
from django.test import TestCase
from .urls import logout, login, registration, members_home, about_page, non_members_home


class TestURLS(TestCase):
    
    # Tests the different URL patterns, and confirms they can be found  
    def test_urlpatterns(self):
        found = resolve('/accounts/login/')
        self.assertEqual(found.func, login)

        found = resolve('/accounts/logout/')
        self.assertEqual(found.func, logout)

        found = resolve('/accounts/register/')
        self.assertEqual(found.func, registration)
        
        found = resolve('/accounts/members_home/')
        self.assertEqual(found.func, members_home)
        
        found = resolve('/accounts/about/')
        self.assertEqual(found.func, about_page)
        
        found = resolve('/accounts/non_members_home/')
        self.assertEqual(found.func, non_members_home)