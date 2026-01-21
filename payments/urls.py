from django.urls import path
from .views import PaymentDetailView, ReleasePaymentView

urlpatterns = [
    path('<int:pk>/', PaymentDetailView.as_view()),
    path('<int:pk>/release/', ReleasePaymentView.as_view()),
]
