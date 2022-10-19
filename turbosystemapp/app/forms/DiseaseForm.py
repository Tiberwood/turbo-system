from django import forms
from ..models import Disease

class DiseaseForm(forms.ModelForm):
  name = forms.CharField(max_length=50)
  description = forms.CharField(max_length=100)
  class Meta:
    model = Disease
    fields = ['name', 'description']