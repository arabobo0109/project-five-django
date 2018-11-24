from django.test import TestCase

class TestViews(TestCase):
    
    # Tests the urls return a valid status code.
    def test_all_products(self):
        page = self.client.get("/content/")
        self.assertEqual(page.status_code, 200)
    
    def test_product_detail(self):
        page = self.client.get("/content/")
        self.assertEqual(page.status_code, 200)