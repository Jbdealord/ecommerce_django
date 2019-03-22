from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='test@jatinkaushik.com', password='asdfghjkl123'):
    """create a sample user"""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):

        email = 'iam@jatinkaushik.com'
        password = 'jk'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalization(self):

        email = "iam@JATINKAUSHIK.COM"
        user = get_user_model().objects.create_user(email, 'asdfghjkl')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None)

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'iam@jatinkaushik.com',
            'asdfghjkl'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    def test_tag_str(self):
        """test the tag string representation"""
        tag = models.Tag.objects.create(
            user = sample_user(),
            name = 'Vegan'
        )
        self.assertEqual(str(tag), tag.name)