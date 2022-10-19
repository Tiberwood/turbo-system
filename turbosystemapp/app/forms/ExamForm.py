from django import forms
from ..models import Exam, Disease

class CustomDiseases(forms.ModelMultipleChoiceField):
  def label_from_instance(self, member):
    return '%s' % member.name

class ExamForm(forms.ModelForm):
  name = forms.CharField(max_length=100)
  description = forms.CharField(max_length=100)
  file = forms.FileField()
  diseases = CustomDiseases(queryset=Disease.objects.all(),
                            widget=forms.CheckboxSelectMultiple)
  
  class Meta:
    model = Exam
    fields = ['name', 'description', 'file', 'diseases']