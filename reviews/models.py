from django.db import models
from services.models import ServiceRequest

class Review(models.Model):
    service = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
