from django.test import TestCase
from django.contrib.auth import login
from django.contrib.auth.models import User
from ecommerce.models import Product
from django.contrib.messages import get_messages


class TestViews(TestCase):

    # Tests that the checkout function works with correct card details, and that it returns a 200 page status code, that contains the correct HTML, and also returns the correct message.
    def test_checkout_correct_details(self):
            user = User.objects.create_user(username='test', email='test@tester.com', password='testing')
            product = Product(name="This is a test", strap="Yet again, this is a test", description="More text about this being just a test", upvotes="2", tag="meta", target="100.00", remaining="99.00", tribute="20.00", status="W")
            product.save()
            self.client.login(username='test', password='testing')
            self.client.post('/cart/add/{0}'.format(product.id), {'quantity': '50'}, follow=True)
            stripe_id = 'tok_visa'
            
            page = self.client.post('/checkout/', {'full_name':'test','phone_number':'030332999', 'street_address1':'nowhere', 'street_address2':'definitely nowhere', 'town_or_city':'merseyside', 'county':'Liverpool', 'country':'UK','postcode':'wa10 293', 'credit_card_number': '4242424242424242','cvv':'100', 'expiry_month':'12','expiry_year':'2019', 'stripe_id':stripe_id}, follow=True)
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'products.html', 'base.html')
            self.assertContains(page, 'Premium Content')
            self.assertNotContains(page, 'The page does not contain this')
            messages = list(page.context['messages'])
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), 'Your payment was successful, thank you')