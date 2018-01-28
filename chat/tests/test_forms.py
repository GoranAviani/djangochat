from django.test import TestCase

# Create your tests here.

from chat.forms import user_registration_form

class Registration_Form_Test(TestCase):

    # Valid Form Data
    def test_RegistrationForm_valid(self):
        form = user_registration_form(data={'username': "user1", 'password1': "2008user", 'password2': "2008user",})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_RegistrationForm_invalid(self):
        form = user_registration_form(data={'username': "user1", 'password1': "2008user", 'password2': "208useerr"})
        self.assertFalse(form.is_valid())
