from django.shortcuts import render
from rest_framework import viewsets
from .models import Geolocation
from .serializers import GeolocationSerializer
from rest_framework import permissions


class GeolocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Geolocation to be viewed or edited.
    """
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post']
