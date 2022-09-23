from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm

def index(request):
  return render(request, 'app/index.html')

def login_view(request):
  if request.method == 'POST':    
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
      login(request, user)
      return render(request, 'app/index.html')
    else:
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
  print(request.POST)
  form = UserForm(request.POST or None)
  if form.is_valid():
    user = form.save(commit=False)
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user.set_password(password)
    user.save()
    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
        return render(request, 'app/index.html')
  context = {
    "form": form,
  }
  return render(request, 'app/register.html', context)