from django.test import TestCase
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    
    # Tests the urls return a valid status code.
    def test_get_posts(self):
        page = self.client.get("/content/")
        self.assertEqual(page.status_code, 200)
    
    def test_content_detail(self):
        page = self.client.get("/content/")
        self.assertEqual(page.status_code, 200)