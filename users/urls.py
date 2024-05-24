from django.urls import path
from .views import  RegisterView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]