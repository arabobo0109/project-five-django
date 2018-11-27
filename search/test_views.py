from django.test import TestCase

class TestViews(TestCase):
    
    # Tests the urls return a valid status code, and asserts that the correct template is used, and the correct html has been used on each page.
    def do_search_products(self):
        page = self.client.get("/search/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'products.html')
        self.assertContains(page, 'Premium Content')
        self.assertNotContains(page, 'The page does not contain this')