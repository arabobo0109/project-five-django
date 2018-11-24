from django.test import TestCase
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
    
    # Tests the urls return a valid status code, and assert that the correct template is used
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')
        
    def test_login(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')
    
    def test_registration(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration.html')
        
    def test_nonmembershome(self):
        page = self.client.get("/accounts/non_members_home/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'nonmembershome.html')
    
    def test_about(self):
        page = self.client.get("/accounts/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'about.html')