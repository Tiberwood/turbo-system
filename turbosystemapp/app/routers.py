
from django.urls import path, include
from rest_framework import routers
from app.viewsets.PersonViewset import PersonViewset

router = routers.DefaultRouter()

router.register(r'persons', PersonViewset, basename='persons')

urlpatterns = [
  path(r'', include(router.urls)),
]