from django.test import TestCase
from .models import Product

class TestOrder(TestCase):
    
    # Creates a test order, and asserts that the details are correct.
    def test_create_test_product(self):
        item = Product(name="This is a test", strap="Yet again, this is a test", description="More text about this being just a test", upvotes="2", tag="meta", target="100.00", remaining="99.00", tribute="20.00", status="W")
        item.save()
    
        self.assertEqual(item.name, "This is a test")
        self.assertEqual(item.strap, "Yet again, this is a test")
        self.assertEqual(item.description, "More text about this being just a test")
        self.assertEqual(item.upvotes, "2")
        self.assertEqual(item.tag, "meta")
        self.assertEqual(item.target, "100.00")
        self.assertEqual(item.remaining, "99.00")
        self.assertEqual(item.tribute, "20.00")
        self.assertEqual(item.status, "W")
        
        
    # Creates a test order, and asserts that the details are incorrect
    def test_create_wrong_test_product(self):
        item = Product(name="This is a test", strap="Yet again, this is a test", description="More text about this being just a test", upvotes="2", tag="meta", target="100.00", remaining="99.00", tribute="20.00", status="W")
        item.save()
    
        self.assertNotEqual(item.name, "This is a big test")
        self.assertNotEqual(item.strap, "Yet again, this is a tester")
        self.assertNotEqual(item.description, "More text about this being just a test, just a test")
        self.assertNotEqual(item.upvotes, "200")
        self.assertNotEqual(item.tag, "metal")
        self.assertNotEqual(item.target, "1000.00")
        self.assertNotEqual(item.remaining, "99.99")
        self.assertNotEqual(item.status, "WEW")