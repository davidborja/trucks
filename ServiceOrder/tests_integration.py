from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Vehicle.models import Vehicle
from ServiceOrder.models import ServiceOrder, MaintenancePart

class ServiceOrderIntegrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()



    def test_service_order_service(self):
        vehicle = Vehicle.objects.create(brand='Toyota', model='Corolla', year=2020)
        part1 = MaintenancePart.objects.create(name='Engine')
        part2 = MaintenancePart.objects.create(name='Brakes')
        new_service_order_data = {'vehicle': vehicle.id, 'description': 'Routine check', 'date': '2024-05-10', 'parts_involved' : [{'id': str(part1.id), 'name': 'Engine'}, {'id': str(part2.id), 'name': 'Brakes'}, {'name': 'Transmission'}]}
        response = self.client.post(reverse('serviceorder-list'), new_service_order_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        service_order_id = response.data['id']

        response = self.client.get(reverse('serviceorder-detail', args=[service_order_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Routine check')
        self.assertEqual(str(response.data['date']), '2024-05-10')
        self.assertEqual(response.data['state'], 'PEN')


        updated_service_order_data = {'state': 'COMPLETED'}
        response = self.client.put(reverse('serviceorder-detail', args=[service_order_id]), updated_service_order_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(reverse('serviceorder-detail', args=[service_order_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

