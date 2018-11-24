from django.test import TestCase
from .models import Product

from django.test import TestCase

class TestDjango(TestCase):
    
    # Tests whether the tests are working
    def test_is_thing_on(self):
        self.assertEqual(1, 1)


class ProductTests(TestCase):
    
    # Tests for our product models
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')