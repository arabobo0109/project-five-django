from django.test import TestCase

class TestViews(TestCase):
    
    # Tests the urls return a valid status code, and asserts that the correct template is used, and the correct html has been used on each page.
    def test_get_content(self):
        page = self.client.get("/content/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'content.html')
        self.assertContains(page, 'Blog')
        self.assertNotContains(page, 'The page does not contain this')
    
    def test_content_detail(self):
        page = self.client.get("/content/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'content.html', 'base.html')
        self.assertContains(page, 'Blog')
        self.assertNotContains(page, 'The page does not contain this')