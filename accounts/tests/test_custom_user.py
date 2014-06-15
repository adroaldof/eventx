from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.utils import override_settings


@override_settings(AUTH_USER_MODEL='accounts.User')
class FunctionalCustomUserTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        user = UserModel(cpf='12345678901')
        user.set_password('testpassword')
        user.save()

    def test_login_with_cpf(self):
        'Test login with cpf'
        self.assertTrue(self.client.login(
            cpf='12345678901', password='testpassword')
        )
