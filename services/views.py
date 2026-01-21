from rest_framework import generics
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

class ServiceRequestCreateView(generics.CreateAPIView):
    serializer_class = ServiceRequestSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class ServiceRequestListView(generics.ListAPIView):
    serializer_class = ServiceRequestSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'technician':
            return ServiceRequest.objects.filter(technician=user)
        return ServiceRequest.objects.filter(client=user)
