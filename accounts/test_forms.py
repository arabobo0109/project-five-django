from django.test import TestCase
from .forms import UserRegistrationForm

class test_UserLoginForm(TestCase):
    
    # Tests form is valid with all fields correctly filled in
    def test_with_all_fields(self):
        form = UserRegistrationForm({'email': 'test@testing.com', 'username': 'tester', 'password1': 'testing1234', 'password2': 'testing1234'})
        self.assertTrue(form.is_valid())
    
    # Tests form is not valid when password confirmation is missing, and confirms correct error message is displayed
    def test_password_missing(self):
        form = UserRegistrationForm({'email': 'sarahlouisecrosby@gmail.com', 'username': 'tester', 'password1': 'testing1234', 'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'This field is required.'])
    
    # Tests that form is not valid when passwords don't match, and that the correct error message is displayed
    def test_different_passwords(self):
        form = UserRegistrationForm({'email': 'sarahlouisecrosby@gmail.com', 'username': 'tester', 'password1': 'testing1234', 'password2': 'testing123'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['Passwords must match'])