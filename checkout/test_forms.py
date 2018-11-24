from django.test import TestCase
from .forms import OrderForm

class test_OrderForm(TestCase):
    
    def test_with_all_fields(self):
        form = OrderForm({'full_name' : 'Tester', 'phone_number' : '999999', 'country' : 'UK', 'postcode' : 'wu2 2ue', 'town_or_city' : 'Testing', 'street_address1' : 'nowhere', 'street_address2' : 'nowhere town', 'county' : 'merseyside'})
        self.assertTrue(form.is_valid())
        
    def test_with_missing_name(self):
        form = OrderForm({'full_name' : '', 'phone_number' : '999999', 'country' : 'UK', 'postcode' : 'wu2 2ue', 'town_or_city' : 'Testing', 'street_address1' : 'nowhere', 'street_address2' : 'nowhere town', 'county' : 'merseyside'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])