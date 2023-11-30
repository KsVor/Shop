from http import HTTPStatus
from datetime import timedelta
from django.utils.timezone import now

from django.test import TestCase
from django.urls import reverse

from users.models import User, EmailVerification

class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'aaa', 'last_name': 'aaa',
            'username': 'kit12', 'email': 'ksvoronova81@gmail.com',
            'password1': 'kseniya2002+', 'password2': 'kseniya2002+'
        }
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store = Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(User.objects.filter(username=username).exists())

        email_vetification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_vetification.exists())
        self.assertEqual(email_vetification.first().expiration.date(), (now() + timedelta(hours=48)).date())