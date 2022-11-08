from django import forms
from ..models import Patient

class PatientForm(forms.ModelForm):
  
  # def __init__(self, *args, **kwargs):
  #   self.request = kwargs.pop('request')
  #   super(PatientForm, self).__init__(*args, **kwargs)
  #   self.fields['diagnostics'].queryset = self.request.user.diagnostics.all()
  
  name = forms.CharField(label='Name', max_length=250)
  last_name = forms.CharField(label='Last Name', max_length=250)
  birthday = forms.DateField(label='Birthday')
  
  class Meta:
    model = Patient
    fields = ['name', 'last_name', 'birthday', 'diagnostics']