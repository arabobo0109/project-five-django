from django.test import TestCase
from .models import Order

class TestOrder(TestCase):
    
    # Creates a test order, and asserts that the details are correct.
    def test_create_test_order(self):
        item = Order(full_name="Testing Tester", phone_number="0292930302", country="UK", postcode="uwo93oe", town_or_city="Merseyside", street_address1="nowhere", street_address2="definitely nowhere", county="Merseyside", date="2019-12-12")
        item.save()
    
        self.assertEqual(item.full_name, "Testing Tester")
        self.assertEqual(item.phone_number, "0292930302")
        self.assertEqual(item.country, "UK")
        self.assertEqual(item.postcode, "uwo93oe")
        self.assertEqual(item.town_or_city, "Merseyside")
        self.assertEqual(item.street_address1, "nowhere")
        self.assertEqual(item.street_address2, "definitely nowhere")
        self.assertEqual(item.county, "Merseyside")
        self.assertEqual(item.date, "2019-12-12")
        
        
    def test_create_test_order(self):
        
        # Creates a test order, and asserts that the details are incorrect
        item = Order(full_name="Testing Tester", phone_number="0292930302", country="UK", postcode="uwo93oe", town_or_city="Merseyside", street_address1="nowhere", street_address2="definitely nowhere", county="Merseyside", date="2019-12-12")
        item.save()
    
        self.assertNotEqual(item.full_name, "Not my real name")
        self.assertNotEqual(item.phone_number, "02929302302")
        self.assertNotEqual(item.country, "")
        self.assertNotEqual(item.postcode, "postacode")
        self.assertNotEqual(item.town_or_city, "Liverpool")
        self.assertNotEqual(item.street_address1, "here")
        self.assertNotEqual(item.street_address2, "maybenowhere")
        self.assertNotEqual(item.county, "Liverpool")
        self.assertNotEqual(item.date, "2019-12-11")