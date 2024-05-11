from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Vehicle.models import Vehicle

class VehicleIntegrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_vehicle_service(self):
        new_vehicle_data = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020}
        response = self.client.post(reverse('vehicle-list'), new_vehicle_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        vehicle_id = response.data['id']


        response = self.client.get(reverse('vehicle-detail', args=[vehicle_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['brand'], 'Toyota')
        self.assertEqual(response.data['model'], 'Corolla')
        self.assertEqual(response.data['year'], 2020)


        updated_vehicle_data = {'brand': 'Honda', 'year': 2024, 'model':'Corolla'}
        response = self.client.put(reverse('vehicle-detail', args=[vehicle_id]), updated_vehicle_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(reverse('vehicle-detail', args=[vehicle_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



