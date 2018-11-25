from django.apps import apps
from django.test import TestCase
from .apps import AccountsConfig


class TestAccountsConfig(TestCase):

    def test_app(self):
        self.assertEqual("accounts", AccountsConfig.name)
        self.assertEqual("accounts", apps.get_app_config("accounts").name)