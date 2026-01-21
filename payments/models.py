from django.db import models
from services.models import ServiceRequest

class Payment(models.Model):
    STATUS_CHOICES = (
        ('held', 'Held'),
        ('released', 'Released'),
        ('refunded', 'Refunded'),
    )

    service = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='held')
    created_at = models.DateTimeField(auto_now_add=True)
