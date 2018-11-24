from django.test import TestCase

class TestViews(TestCase):
    
    # Tests the urls return a valid status code, and assert that the correct template is used
    def do_search_products(self):
        page = self.client.get("/search/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'products.html')