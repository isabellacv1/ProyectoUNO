from django.urls import path
from .views import ServiceRequestCreateView, ServiceRequestListView

urlpatterns = [
    path('create/', ServiceRequestCreateView.as_view()),
    path('', ServiceRequestListView.as_view()),
]
