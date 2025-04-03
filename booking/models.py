from django.db import models
from django.contrib.auth.models import User

class Turf(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.turf.name} booked by {self.user.username} on {self.booking_date}"
