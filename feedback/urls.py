from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedbackModelViewSet

router = DefaultRouter()
router.register(r"", FeedbackModelViewSet, basename="feedback")

urlpatterns = [
    path("", include(router.urls)),
]