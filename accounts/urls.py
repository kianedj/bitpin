from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UsersAPIView, MyTokenObtainPairView

urlpatterns = [
    path('', UsersAPIView.as_view({'list': 'post', 'list': 'get'})),
    path('login/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
