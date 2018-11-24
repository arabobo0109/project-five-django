from django.test import TestCase
from .models import Content

class TestOrder(TestCase):
    
    # Creates a test order, and asserts that the details are correct.
    def test_create_test_content(self):
        item = Content(title="This is a test", strapline="Yet again, this is a test", article="More text about this being just a test", published_date="2019-12-12", views="2", tag="meta")
        item.save()
    
        self.assertEqual(item.title, "This is a test")
        self.assertEqual(item.strapline, "Yet again, this is a test")
        self.assertEqual(item.article, "More text about this being just a test")
        self.assertEqual(item.published_date, "2019-12-12")
        self.assertEqual(item.views, "2")
        self.assertEqual(item.tag, "meta")
        
    # Creates a test order, and asserts that the details are incorrect
    def test_create_test_content(self):
        item = Content(title="This is a test", strapline="Yet again, this is a test", article="More text about this being just a test", published_date="2019-12-12", views="2", tag="meta")
        item.save()
    
        self.assertNotEqual(item.title, "This is a big test")
        self.assertNotEqual(item.strapline, "Yet again, this is a tester")
        self.assertNotEqual(item.article, "More text about this being just a test, just a test")
        self.assertNotEqual(item.published_date, "2020-12-12")
        self.assertNotEqual(item.views, "200")
        self.assertNotEqual(item.tag, "metal")