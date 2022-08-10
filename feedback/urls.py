from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FeedbackModelViewSet, FeedbackTypeModelViewSet

router = DefaultRouter()
router.register(r"feedback-type", FeedbackTypeModelViewSet, basename="feedback-type")
router.register(r"", FeedbackModelViewSet, basename="feedback")

urlpatterns = [
    path("", include(router.urls)),
]
