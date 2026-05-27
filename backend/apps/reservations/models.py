from django.db import models

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    table = models.ForeignKey('tables.Table', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    deposit = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
