from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Payment
from .serializers import PaymentSerializer

class PaymentDetailView(generics.RetrieveAPIView):
    """
    Devuelve la información del pago asociado a un servicio
    (estado escrow, monto, comisión, etc.)
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ReleasePaymentView(APIView):
    """
    Libera el pago cuando el cliente confirma el servicio
    """

    def post(self, request, pk):
        try:
            payment = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response(
                {"error": "Payment not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if payment.status != 'held':
            return Response(
                {"error": "Payment already processed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔓 Liberar pago
        payment.status = 'released'
        payment.save()

        return Response(
            {"message": "Payment released successfully"},
            status=status.HTTP_200_OK
        )
