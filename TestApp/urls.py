from django.urls import path

from TestApp.views import UserView, UserRegister
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('view/<int:pk>/', UserView.as_view()),
    path('pview/', UserRegister.as_view()),
    path('token-generator/', obtain_auth_token),
    path('token-obtain/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view())
]