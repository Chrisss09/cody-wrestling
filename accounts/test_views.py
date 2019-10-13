from django.test import TestCase
from .models import UserRegistrationModel

class TestViews(TestCase):
    def test_get_homepage(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')

    def test_get_login_page(self):
        page = self.client.get('/accounts/accounts/login/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')

    def test_get_registration_page(self):
        page = self.client.get('/accounts/accounts/registration/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration.html')

    def test_get_password_reset_page(self):
        page = self.client.get('/accounts/accounts/password_reset/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration/password_reset_form.html')

    def test_get_confirm_password_reset_page(self):
        page = self.client.get('/accounts/accounts/password_reset/done/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration/password_reset_done.html')

    def test_get_set_password_page(self):
        page = self.client.get('/accounts/accounts/reset/MQ/set-password/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration/password_reset_confirm.html')

    def test_get_password_complete_page(self):
        page = self.client.get('/accounts/accounts/reset/done/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration/password_reset_complete.html')