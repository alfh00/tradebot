from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserAPIKeyViewSet

router = DefaultRouter()
router.register(r'api-keys', UserAPIKeyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
