from django.test import TestCase

class TestViews(TestCase):
    
    # Tests the urls return a valid status code, and assert that the correct template is used
    def test_get_content(self):
        page = self.client.get("/content/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'content.html')
    
    def test_content_detail(self):
        page = self.client.get("/content/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'content.html', 'base.html')