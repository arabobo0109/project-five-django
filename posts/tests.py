from django.test import TestCase

class TestDjango(TestCase):
    
    # Tests whether the tests are working
    def test_is_thing_on(self):
        self.assertEqual(1, 1)
