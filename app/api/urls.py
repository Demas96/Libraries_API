from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import parser, LibrariesViewSet


router = routers.SimpleRouter()
router.register(r'libraries', LibrariesViewSet)
urlpatterns = [
    path('parser/', parser),
    path('v1/', include(router.urls)),
]