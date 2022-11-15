from django.shortcuts import render
from ..models import Disease
from ..forms.DiseaseForm import DiseaseForm

def index(request):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  return render(request, 'app/index.html')

def create_diasese(request):
  if not request.user.is_authenticated and request.user.is_admin:
    return render(request, 'app/login.html')
  form = DiseaseForm(request.POST or None)
  if form.is_valid():
    try:
      disease = Disease.objects.get(name=form.cleaned_data['name'])
      if disease:
        context = {
          'form': form,
          'error_message': 'Disease already exists'
        }
        return render(request, 'app/register_disease.html', context)
    except Disease.DoesNotExist:
      disease = form.save(commit=False)
      disease.save()
      return render(request, 'app/index.html', { 'message': 'Disease created successfully' })
  context = {
    'form': form,
  }
  return render(request, 'app/create_disease.html', context)