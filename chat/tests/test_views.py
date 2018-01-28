from django.test import TestCase

# Create your tests here.
from chat.models import Message
from django.urls import reverse


class dashboardViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_messages = 13
        for message_num in range(number_of_messages):
            Message.objects.create(message_text='aaaaaaaaaaaaaaaa %s' % message_num, message_users = '1/2 %s' % message_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/dashboard/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('dashboard'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('dashboard'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'dashboard.html')
        
