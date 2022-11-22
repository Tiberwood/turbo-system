from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from ..models import Patient, Diagnostic

from ..forms.PatientForm import PatientForm
from ..forms.ExamForm import ExamForm

from ..filters.PatientFilter import PatientFilter

from ..utils.validators import validate_file_extension


def patient_list(request):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  user_model = get_user_model()
  if request.user.is_superuser:
    patients = user_model.objects.filter(is_patient=True)
    context = {
      'patients': patients
    }
    return render(request, 'app/patient_list.html', context)
  if request.user.is_doctor:
    doctor_instance = user_model.objects.get(pk=request.user.id)
    patients = Patient.objects.filter(diagnostics__recepient=doctor_instance.pk)
    context = {
      'patients': patients
    }
    return render(request, 'app/patient_list.html', context)
  
def create_patient(request):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  user_model = get_user_model()
  # patient = get_object_or_404(user_model, email=form.cleaned_data['email'])
  form = PatientForm(request.POST or None)
  if form.is_valid():
    patient = form.save(commit=False)
    patient.save()
    return render(request, 'app/index.html', { 'message': 'Patient created successfully' })
  
  context = {
    'form': form,
  }  
  return render(request, 'app/register_patient.html', context)

def upload_exam(request, diagnostic_id):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  form = ExamForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    try:
      if validate_file_extension(request.FILES['file'].name):
        exam = form.save(commit=False)
        exam.save()
        diagnostic_instante = Diagnostic.objects.get(pk=diagnostic_id)
        diagnostic_instante.exams.add(exam)
        diagnostic_instante.save()
        return render(request, 'app/index.html', { 'message': 'Exam created successfully' })
    except Diagnostic.DoesNotExist:
      return render(request, 'app/upload_exam.html', { 'message': 'Diagnostic does not exist' })
    except:
      context = {
        'form': form,
        'error_message': 'Invalid file'
      }
      return render(request, 'app/upload_exam.html', context)
  context = {
    'form': form,
  }
  return render(request, 'app/upload_exam.html', context)

def exam_list(request, patient_id, diagnostic_id):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  try:
    user_model = get_user_model()
    patient = get_object_or_404(user_model, pk=patient_id)
    diagnostic = get_object_or_404(Diagnostic, pk=diagnostic_id)
  except user_model.DoesNotExist:
    return render(request, 'app/exam_list.html', { 'message': 'Patient does not exist' })
  
  context = {
    'patient': patient,
    'exams': diagnostic.exams.all(),
    'diagnostic': diagnostic,
  }
  return render(request, 'app/exam_list.html', context)

def patient_diagnostics(request, patient_id):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  diagnostics = Diagnostic.objects.filter(patient=patient_id)
  context = {
    'diagnostics': diagnostics
  }
  return render(request, 'app/patient_diagnostics.html', context)

def find_patient(request):
  user_model = get_user_model()
  import pdb; pdb.set_trace()
  filter = PatientFilter(request.GET, queryset=user_model.objects.filter(is_patient=True))
  return render(request, 'app/find_patient.html', {'filter': filter})