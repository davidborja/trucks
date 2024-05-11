from django.db import models
from Vehicle.models import Vehicle

# Create your models here.

class MaintenancePart(models.Model):
    name = models.CharField(max_length=100)

class ServiceOrder(models.Model):
    PENDING = 'PEN'
    IN_PROGRESS = 'PRO'
    COMPLETED = 'COM'
    
    MAINTENANCE_STATES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    state = models.CharField(max_length=3, choices=MAINTENANCE_STATES, default=PENDING)
    parts_involved = models.ManyToManyField(MaintenancePart)