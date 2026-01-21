from rest_framework import generics
from .models import TechnicianProfile
from .serializers import TechnicianProfileSerializer

class TechnicianProfileView(generics.RetrieveAPIView):
    queryset = TechnicianProfile.objects.all()
    serializer_class = TechnicianProfileSerializer
