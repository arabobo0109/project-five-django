from django.test import TestCase

class TestViews(TestCase):
    
    # Tests the urls return a valid status code, and assert that the correct template is used
    def test_view_cart(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')