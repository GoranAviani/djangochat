from django.test import TestCase

# Create your tests here.
from chat.models import Message

class MessageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls): #We then call setUpTestData() to create an author object that we will use but not modify in any of the tests.
        #Set up non-modified objects used by all test methods
        Message.objects.create(message_text='Baaaaaaaaaig', message_users='1/2')

    def test_message_text_max_length(self):
        message=Message.objects.get(id=1)
        max_length = message._meta.get_field('message_text').max_length
        self.assertEquals(max_length,10000)

    def test_message_users_max_length(self):
        message=Message.objects.get(id=1)
        max_length = message._meta.get_field('message_users').max_length
        self.assertEquals(max_length,200)
