from rest_framework import serializers
from .models import Geolocation

class GeolocationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        post_like = Geolocation.objects.create(**validated_data)
        return post_like

    class Meta:
        model = Geolocation
        fields = '__all__'


class CreateGeolocation(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['user_geolocation', 'holidays']
