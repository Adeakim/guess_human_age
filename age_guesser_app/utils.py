import requests
from datetime import datetime
from django.core.cache import cache

class AgeGuesserUtils:
    @staticmethod
    def get_age_from_agify(name):
        agify_api_url = f"https://api.agify.io/?name={name}"
        response = requests.get(agify_api_url)
        response.raise_for_status() 
        data = response.json()
        return data['age']

    @staticmethod
    def calculate_date_of_birth(age):
        current_year = datetime.now().year
        return current_year - age

    @staticmethod
    def get_cached_response(name):
        return cache.get(name)
    

    @staticmethod
    def cache_response(name, response_content, timeout=86400):
        cache.set(name, response_content, timeout)
