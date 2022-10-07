import pdb
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms.UserForm import UserForm

def index(request):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  return render(request, 'app/index.html')

def login_view(request):
  if request.method == 'POST':
    try:
      user_model = get_user_model()
      user = user_model.objects.get(email=request.POST['email'])
      if user is not None and user.check_password(request.POST['password']):
        login(request, user)
        return render(request, 'app/index.html')
      else:
        return render(request, 'app/login.html', {'error_message': 'Invalid login'})
    except user_model.DoesNotExist:
      return render(request, 'app/login.html', {'error_message': 'Invalid login'})
    
  return render(request, 'app/login.html')

def logout_view(request):
  logout(request)
  form = UserForm(request.POST or None)
  context = {
    "form": form,
  }
  return render(request, 'app/login.html', context)

def register(request):
  form = UserForm(request.POST or None)
  if form.is_valid():
    user = form.save(commit=False)
    username = form.cleaned_data['username']
    password = form.cleaned_data['password1']
    user.set_password(password)
    user.save()
    user = authenticate(username=username, password=password)
    if user is not None:
      return render(request, 'app/index.html')
  context = {
    "form": form,
  }
  return render(request, 'app/register.html', context)

def patient_list(request):
  user_model = get_user_model()
  patients = user_model.objects.filter(is_patient=True)
  context = {
    'patients': patients
  }
  return render(request, 'app/patient_list.html', context)