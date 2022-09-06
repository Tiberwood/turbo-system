from rest_framework.viewsets import ModelViewSet
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.serializers.PersonSerializer import PersonSerializer

class PersonViewset(ModelViewSet):
  serializer_class = PersonSerializer
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    return self.request.user.persons.all()