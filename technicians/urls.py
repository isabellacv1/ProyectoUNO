from django.urls import path
from .views import TechnicianProfileView

urlpatterns = [
    path('<int:pk>/', TechnicianProfileView.as_view()),
]
