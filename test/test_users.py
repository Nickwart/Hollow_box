from django.test import TestCase
from user_profile.views import CreateUser
from rest_framework.test import APIRequestFactory


class CrateUserTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_user_creation(self):
        user_data = {
            "username": "Ferrumodial",
            "first_name": "Liza",
            "last_name": "old classmate",
            "email": "p-serpenter@gmail.com",
            "password": "qwert1212",
        }
        request = self.factory.post('moderator/createuser', user_data, format='json')
        response = CreateUser.as_view()(request)
        data = {k: v for k, v in response.data.items() if user_data.get(k)}

        self.assertEqual(data, user_data)
