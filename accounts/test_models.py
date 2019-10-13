from django.test import TestCase
from .models import UserRegistrationModel

class TestUserRegModel(TestCase):
    def test_done_defaults_to_false(self):
        new_user = UserRegistrationModel(username='Daniel')
        new_user.save()
        self.assertEqual(new_user.username, 'Daniel')
        self.assertFalse(new_user.is_staff)

    def test_user_as_a_string(self):
        new_user = UserRegistrationModel(username='Daniel')
        self.assertEqual('Daniel', str(new_user))