from rest_framework import serializers
from ServiceOrder.models import ServiceOrder, MaintenancePart

class MaintenancePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenancePart
        fields = ['id', 'name']

class ServiceOrderSerializer(serializers.ModelSerializer):
    parts_involved = MaintenancePartSerializer(many=True)

    class Meta:
        model = ServiceOrder
        fields = ['id', 'vehicle', 'description', 'date', 'state', 'parts_involved']

    def create(self, validated_data):
        parts_data = validated_data.pop('parts_involved')
        service_order = ServiceOrder.objects.create(**validated_data)
        for part_data in parts_data:
            part, _ = MaintenancePart.objects.get_or_create(**part_data)
            service_order.parts_involved.add(part)
        return service_order

    def update(self, instance, validated_data):
        parts_data = validated_data.pop('parts_involved')
        instance = super().update(instance, validated_data)
        instance.parts_involved.clear()
        for part_data in parts_data:
            part, _ = MaintenancePart.objects.get_or_create(**part_data)
            instance.parts_involved.add(part)
        return instance