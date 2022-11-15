from django.shortcuts import render
from django.contrib.auth import get_user_model

from ..forms import DiagnosticForm

from ..models import Diagnostic

def doctor_list(request):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  if request.user.is_doctor:
    context = {
      'message': 'No tan rápido cerebrito'
    }
    return render(request, 'app/403.html', context)
  user_model = get_user_model()
  if request.user.is_superuser:
    doctors = user_model.objects.filter(is_doctor=True)
    context = {
      'doctors': doctors
    }
    return render(request, 'app/doctor_list.html', context)
  if request.user.is_patient:
    doctors = Diagnostic.objects.filter(patient=request.user).annotate(doctors=Count('recepient'))
    context = {
      'doctors': doctors,
    }
    return render(request, 'app/doctor_list.html', context)
  
def create_diagnostic(request, patient_id):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  if not request.user.is_doctor or not request.user.is_superuser:
    context = {
      'message': 'No tan rápido cerebrito'
    }
    return render(request, 'app/403.html', context)
  form = DiagnosticForm(request.POST or None)
  if form.is_valid():
    diagnostic = form.save(commit=False)
    diagnostic.recepient = request.user
    diagnostic.patient = patient_id
    diagnostic.save()
    return render(request, 'app/index.html', { 'message': 'Diagnostic created successfully' })
  context = {
    'form': form,
  }
  return render(request, 'app/create_diagnostic.html', context)