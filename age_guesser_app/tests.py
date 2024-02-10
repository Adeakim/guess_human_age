from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import datetime, timedelta
from .utils import AgeGuesserUtils

class GetBayiiAgeViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_valid_request(self):
        '''Test a valid request with a new name'''

        name = "john"
        age = 25
        date_of_birth = datetime.now().year - age

        AgeGuesserUtils.get_age_from_agify = lambda x: age
        AgeGuesserUtils.calculate_date_of_birth = lambda x: date_of_birth
        AgeGuesserUtils.get_cached_response = lambda x: None
        AgeGuesserUtils.cache_response = lambda x, y, timeout=86400: None

        url = reverse('human_age')
        response = self.client.post(url, {"name": name}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], name)
        self.assertEqual(response.data['age'], age)
        self.assertEqual(response.data['date_of_birth'], date_of_birth)

    def test_cached_response(self):
        '''Test that a cached response is returned for the same name'''

        name = "john"
        cached_response = {"name": name, "age": 25, "date_of_birth": datetime.now().year - 25}

        AgeGuesserUtils.get_age_from_agify = lambda x: None
        AgeGuesserUtils.calculate_date_of_birth = lambda x: None
        AgeGuesserUtils.get_cached_response = lambda x: cached_response
        AgeGuesserUtils.cache_response = lambda x, y, timeout=86400: None

        url = reverse('human_age')
        response = self.client.post(url, {"name": name}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, cached_response)

    def test_missing_name(self):
        url = reverse('human_age')
        response = self.client.post(url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)