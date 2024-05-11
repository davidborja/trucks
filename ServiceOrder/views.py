from rest_framework import viewsets
from ServiceOrder.models import ServiceOrder, MaintenancePart
from ServiceOrder.service_order_serializers import ServiceOrderSerializer, MaintenancePartSerializer


class ServiceOrderViewSet(viewsets.ModelViewSet):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer

class MaintenancePartViewSet(viewsets.ModelViewSet):
    queryset = MaintenancePart.objects.all()
    serializer_class = MaintenancePartSerializer
