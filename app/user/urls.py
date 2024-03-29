"""
URL mapping for the user app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserModelViewSet

router = DefaultRouter()
router.register(r'user', UserModelViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
