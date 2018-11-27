from django.test import TestCase
from django.contrib.auth import login
from django.contrib.auth.models import User

class UserTests(TestCase):
    
    # Tests that a user and superuser can be created
    def setUp(self):
        self.test_super_user = User.objects.create_superuser('tester', 'test@testing.com', 'justatest')
        self.test_user = User.objects.create_user('testertester', 'tester@testing.com', 'anothertest')

    def test_users(self):
    
        test_super_user = User.objects.get(username="tester")
        test_user = User.objects.get(username="testertester")
        
        self.assertIsInstance(test_super_user, User)
        self.assertIsInstance(test_user, User)
    
        self.assertTrue(test_super_user.is_superuser)
        self.assertFalse(test_user.is_superuser)
        

class TestViews(TestCase):
    
    # Tests the urls return a valid status code, and asserts that the correct template is used, and the correct html has been used on each page.
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')
        self.assertContains(page, 'A lifestyle blog')
        self.assertNotContains(page, 'The page does not contain this')
        
    def test_login(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')
        self.assertContains(page, 'Log In')
        self.assertNotContains(page, 'The page does not contain this')
    
    def test_registration(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration.html')
        self.assertContains(page, 'Registration')
        self.assertNotContains(page, 'The page does not contain this')
        
    def test_nonmembershome(self):
        page = self.client.get("/accounts/non_members_home/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'nonmembershome.html')
        self.assertContains(page, 'Sorry, but you do not currently have access')
        self.assertNotContains(page, 'The page does not contain this')
    
    def test_about(self):
        page = self.client.get("/accounts/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'about.html')
        self.assertContains(page, 'A brief introduction')
        self.assertNotContains(page, 'The page does not contain this')
        
    def test_members_home(self):
        user = User.objects.create_user(username='test', email='test@tester.com', password='testing')
        page = self.client.login(username='test', password='testing')
        page = self.client.get("/accounts/members_home/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'membershome.html')
        self.assertContains(page, 'Welcome!')
        self.assertNotContains(page, 'The page does not contain this')
        
    # Tests that the logout function performs a redirection, and that it is not a login function
    def test_logout(self):
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)
        self.assertFalse(self.client.login())
        
    
