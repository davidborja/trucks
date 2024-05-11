from django.test import TestCase
from Vehicle.models import Vehicle
from ServiceOrder.models import ServiceOrder, MaintenancePart
from ServiceOrder.service_order_serializers import ServiceOrderSerializer

class ServiceOrderSerializerTestCase(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(brand='Toyota', model='Corolla', year=2020)
        self.part1 = MaintenancePart.objects.create(name='Engine')
        self.part2 = MaintenancePart.objects.create(name='Brakes')
        self.service_order = ServiceOrder.objects.create(vehicle=self.vehicle, description='Routine check', date='2024-05-10')
        self.service_order.parts_involved.set([self.part1, self.part2])
        self.serializer_data = {
            'description': 'Oil change',
            'date': '2024-05-15',
            'state': 'COM',
            'parts_involved': [{'id': self.part1.id, 'name': 'Engine'}, {'id': self.part2.id, 'name': 'Brakes'}, {'name': 'Transmission'}]
        }
        self.length_parts_involved = len(self.serializer_data.get("parts_involved"))

    def test_update_service_order(self):
        serializer = ServiceOrderSerializer(instance=self.service_order, data=self.serializer_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_service_order = serializer.save()
        self.assertEqual(updated_service_order.description, 'Oil change')
        self.assertEqual(str(updated_service_order.date), '2024-05-15')
        self.assertEqual(updated_service_order.state, 'COM')
        self.assertEqual(updated_service_order.vehicle, self.vehicle)
        self.assertEqual(updated_service_order.parts_involved.count(), self.length_parts_involved)
        self.assertTrue(updated_service_order.parts_involved.filter(name='Engine').exists())
        self.assertTrue(updated_service_order.parts_involved.filter(name='Transmission').exists())
