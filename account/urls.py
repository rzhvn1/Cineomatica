from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from .views import (ClubCardModelViewSet, CustomUserRegisterViewSet,
                    LogoutView, UpdatePassword)

router = DefaultRouter()
router.register(r"register", CustomUserRegisterViewSet, basename="register")
router.register(r"club-card", ClubCardModelViewSet, basename="club-card")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("change-password/", UpdatePassword.as_view(), name="change-password"),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
]
