import django_filters
from ..models import User

class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'dni']