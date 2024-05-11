from django.test import TestCase
from .models import Vehicle

class VehicleModelTestCase(TestCase):
    def test_create_vehicle(self):
        vehicle = Vehicle.objects.create(brand='Toyota', model='Corolla', year=2020)
        self.assertEqual(vehicle.brand, 'Toyota')
        self.assertEqual(vehicle.model, 'Corolla')
        self.assertEqual(vehicle.year, 2020)

    def test_vehicle_str_representation(self):
        vehicle = Vehicle.objects.create(brand='Toyota', model='Corolla', year=2020)
        self.assertEqual(str(vehicle), 'Toyota Corolla (2020)')
