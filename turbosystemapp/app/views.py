from django.shortcuts import render
from .forms.DiseaseForm import DiseaseForm
from .models import Disease

def create_diasese(request):
  if not request.user.is_authenticated and request.user.is_admin:
    return render(request, 'app/login.html')
  disease = Disease.objects.get(name=form.cleaned_data['name'])
  form = DiseaseForm(request.POST or None)
  if disease:
    context = {
      'form': form,
      'error_message': 'Disease already exists'
    }
    return render(request, 'app/register_disease.html', context)
  if form.is_valid():
    disease = form.save(commit=False)
    disease.save()
    return render(request, 'app/index.html')
  context = {
    'form': form,
  }
  return render(request, 'app/create_disease.html', context)
