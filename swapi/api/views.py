import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import People, Planet
from api.serializers import PeopleSerializer, PeopleModelSerializer


class PeopleListApiView(APIView):
    """
    People listing actions. Must support the following method:

        * GET: returns the whole list of People objects.

        * POST: creates a new People object using submitted payload.
    """
    pass


class PeopleDetailApiView(APIView):
    """
    People detail actions. Must support the following method:

        * GET: retrieves information about one particular People object.

        * PUT/PATCH: updates (either fully or partially) a specific People
                     object using submitted payload.

        * DELETE: deletes one particular People object.
    """
    pass


class PeopleViewSet(viewsets.ViewSet):
    """
    Implement all required REST actions.

    Follow the default ViewSet method naming convention:
    http://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions

    Use a ModelSerializer instead of a regular Serializer instance.

    Make sure all api.tests still pass.
    """
    pass


class PeopleModelViewSet(viewsets.ModelViewSet):
    """
    Migrate the same logic as above, but using ModelViewSets
    and ModelSerializers.

    Make sure all api.tests still pass.
    """
    pass
