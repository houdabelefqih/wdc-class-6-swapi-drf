from rest_framework import serializers

from api.models import People, Planet


class PeopleSerializer(serializers.Serializer):
    pass


class PeopleModelSerializer(serializers.ModelSerializer):
    pass
