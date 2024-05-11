# maintenance/views.py
from rest_framework import viewsets
from Vehicle.models import Vehicle
from Vehicle.vehicle_serializers import VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

