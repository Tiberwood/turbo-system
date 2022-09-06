from rest_framework.serializers import ModelSerializer
from app.models import Proceedings

class ProceedingsSerializer(ModelSerializer):
  class Meta:
    model = Proceedings
    fields = '__all__'