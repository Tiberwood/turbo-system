from rest_framework.serializers import ModelSerializer
from app.models import Person
from app.serializers.ProceedingSerializer import ProceedingsSerializer

class PersonSerializer(ModelSerializer):
  proceedings = ProceedingsSerializer(many=True, read_only=True)

  class Meta:
    model = Person
    fields = ('id', 'name', 'last_name', 'age', 'email', 'phone', 'address', 'proceedings')