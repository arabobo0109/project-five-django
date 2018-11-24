from django.test import TestCase
from .forms import BoardPostForm

class test_BoardPostForm(TestCase):

    def test_user_not_selected(self):
        form = BoardPostForm({'title' : 'This is just a test case', 'content' : 'I know nothing, except that this is a test case', 'published_date' : '12/12/2003', 'tag' : 'testing', 'user': 'test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['user'], ['Select a valid choice. That choice is not one of the available choices.'])
        
    def test_title_missing(self):
        form = BoardPostForm({'title' : '', 'content' : 'I know nothing, except that this is a test case', 'published_date' : '12/12/2003', 'tag' : 'testing', 'user': 'test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        
    def test_incorrect_date(self):
        form = BoardPostForm({'title' : 'This is just a test case', 'content' : 'I know nothing, except that this is a test case', 'published_date' : 'blahblah', 'tag' : 'testing', 'user': 'test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['published_date'], ['Enter a valid date/time.'])