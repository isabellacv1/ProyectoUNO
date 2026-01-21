from django.db import models
from users.models import User

class TechnicianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document_number = models.CharField(max_length=20)
    verified = models.BooleanField(default=False)
    experience_years = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    completed_services = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
