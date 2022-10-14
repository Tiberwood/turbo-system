
# from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

class UpdateUserForm(forms.ModelForm):
  class Meta:
    model = get_user_model()
    exclude = ('password1',)
    fields = ['username', 'email', 'first_name', 'last_name', 'is_doctor', 'is_patient']