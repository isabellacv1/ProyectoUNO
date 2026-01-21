from decimal import Decimal
from rest_framework import generics

from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from payments.models import Payment
from .utils import get_available_technician


class ServiceRequestCreateView(generics.CreateAPIView):
    serializer_class = ServiceRequestSerializer

    def perform_create(self, serializer):
        # 1️⃣ Crear servicio
        service = serializer.save(client=self.request.user)

        # 2️⃣ Crear pago (escrow mock)
        base_price = Decimal('100000.00')
        commission = base_price * Decimal('0.15')

        Payment.objects.create(
            service=service,
            amount=base_price,
            commission=commission,
            status='held'
        )

        # 3️⃣ Asignación automática de técnico
        technician = get_available_technician()

        if technician:
            service.technician = technician
            service.status = 'assigned'
            service.save()


class ServiceRequestListView(generics.ListAPIView):
    serializer_class = ServiceRequestSerializer

    def get_queryset(self):
        user = self.request.user

        if user.user_type == 'technician':
            return ServiceRequest.objects.filter(technician=user)

        return ServiceRequest.objects.filter(client=user)
