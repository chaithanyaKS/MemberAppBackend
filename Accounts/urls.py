from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .views import ProfileViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="Users")
router.register(r"profile", ProfileViewSet, basename="User-Profile")
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
