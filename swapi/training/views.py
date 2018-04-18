from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, authentication, permissions


@api_view()
def first_drf_view(request):
    """
    Return a simple JSON object.
    """
    pass


@api_view(['GET', 'POST'])
def multi_method_view(request):
    """
    If received a POST request, return a JSON object displaying the submitted payloadself.
    Otherwise, return a simple JSON object showing the request method.
    """
    pass


class FirstClassAPIView(APIView):
    """
    Implement support for GET requests.
    """
    pass


class MultiMethodAPIView(APIView):
    """
    Implement support for GET and POST requests.
    """
    pass


class CustomStatusCode(APIView):
    """
    Return a custom 400 BAD REQUEST status code.
    """
    pass


class CustomHeader(APIView):
    """
    Return a customer `X-RMOTR-IS-AWESOME` response header.
    """
    pass
