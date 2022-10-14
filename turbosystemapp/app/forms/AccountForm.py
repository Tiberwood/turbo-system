
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class AccountForm(UserCreationForm):
  class Meta:
    model = get_user_model()
    exclude = ('is_doctor', 'is_patient',)
    fields = ['username', 'email', 'first_name', 'last_name']