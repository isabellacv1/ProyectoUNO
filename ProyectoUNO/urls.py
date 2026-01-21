from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),

    path('api/users/', include('users.urls')),
    path('api/technicians/', include('technicians.urls')),
    path('api/services/', include('services.urls')),
    path('api/payments/', include('payments.urls')),
]

