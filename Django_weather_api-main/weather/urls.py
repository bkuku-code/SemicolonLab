from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import MyTokenObtainPairView

from . import views

api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]


urlpatterns = [

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/v1/', include(api_urlpatterns)),
    # path('api/', include('accounts.urls')),
    path('api/authuser/weather/',views.authenticatedwetheruser, name='weather_auth_user'),
    path('api/unauthuser/weather/',views.unauthenticatedwetheruser, name='weather_unauth_user'),
    path('api/authuser/weatherd/',views.authenticatedwetheruser_with_days, name='weather_auth_days'),
    path('api/unauthuser/weatherd/',views.unauthenticatedwetheruser_with_days, name='weather_unauth_days'),
  

]