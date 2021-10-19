from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from usersApi.views import UserCreateView, UserDetailView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),      #Loguear Usuario
    path('refresh/', TokenRefreshView.as_view()),       #Renovar acceso al token
    path('user/', UserCreateView.as_view()),            #Registrar Usuario
    path('user/<int:pk>/', UserDetailView.as_view()),   #Obtener información del Usuario
]