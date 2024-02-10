import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import AgeGuesserUtils

class GuessAgeBynameView(APIView):
    def post(self, request):
        try:
            name = request.data.get("name", "").lower()

            if not name:
                return Response({"error": "Name is required in the request."}, status=status.HTTP_400_BAD_REQUEST)
            # caching
            cached_response = AgeGuesserUtils.get_cached_response(name)
            if cached_response:
                return Response(cached_response)
            age = AgeGuesserUtils.get_age_from_agify(name)
            date_of_birth = AgeGuesserUtils.calculate_date_of_birth(age)

            response_content = {"name": name, "age": age, "date_of_birth": date_of_birth}

            # Cache the response for 24 hours
            AgeGuesserUtils.cache_response(name, response_content)

            return Response(response_content)
        except requests.RequestException as e:
            return Response({"error": f"Failed to fetch age: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
