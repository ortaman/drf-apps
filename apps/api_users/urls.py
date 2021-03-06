
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import UserCreateList, UserDetail


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', UserCreateList.as_view(), name="users"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user"),
]
