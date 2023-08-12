from rest_framework import serializers

from airport_api.models import Airport, Route


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ("id", "name", "closest_big_city")


class RouteSerializer(serializers.ModelSerializer):
    source = AirportSerializer(many=False, read_only=False)
    destination = AirportSerializer(many=False, read_only=False)

    class Meta:
        model = Route
        fields = ("source", "destination", "distance")
