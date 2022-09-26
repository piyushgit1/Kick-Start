from django.urls import path, include

from TestApp.views import UserView, UserRegister
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.decorators.cache import cache_page
from . import views
from Test import settings

urlpatterns = [

    path("home/", cache_page(900)(views.homepage)),
    path('view/<int:pk>/', cache_page(60 * 15)(UserView.as_view())),
    path('pview/', UserRegister.as_view()),
    path('token-generator/', obtain_auth_token),
    path('token-obtain/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('debug/', include('debug_toolbar.urls')),
