from django.db import models

class Table(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('dirty', 'Dirty'),
        ('reserved', 'Reserved'),
    ]
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    section = models.CharField(max_length=50, default='Main')
    updated_at = models.DateTimeField(auto_now=True)
