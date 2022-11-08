from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from ..forms.UserForm import UserForm
from ..forms.UpdateUserForm import UpdateUserForm
from ..forms.AccountForm import AccountForm

def register(request):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  form = UserForm(request.POST or None)
  user_model = get_user_model()
  if form.is_valid():
    existing_email = user_model.objects.filter(email=form.cleaned_data['email'])
    if existing_email:
      context = {
        'form': form,
        'error_message': 'Email already exists'
      }
      return render(request, 'app/register.html', context)
    existing_username = user_model.objects.filter(username=form.cleaned_data['username'])
    if existing_username:
      context = {
        'form': form,
        'error_message': 'Username already exists'
      }
      return render(request, 'app/register.html', context)
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

def register_account(request):
  form = AccountForm(request.POST or None)
  user_model = get_user_model()
  if form.is_valid():
    existing_user = user_model.objects.filter(email=form.cleaned_data['email'])
    if existing_user:
      context = {
        'form': form,
        'error_message': 'Email already exists'
      }
      return render(request, 'app/register_user.html', context)
    existing_username = user_model.objects.filter(username=form.cleaned_data['username'])
    if existing_username:
      context = {
        'form': form,
        'error_message': 'Username already exists'
      }
      return render(request, 'app/register_user.html', context)
    user = form.save(commit=False)
    username = form.cleaned_data['username']
    password = form.cleaned_data['password1']
    user.set_password(password)
    user.is_patient = True
    user.save()
    user = authenticate(username=username, password=password)
    if user is not None:
      return render(request, 'app/index.html')
  context = {
    "form": form,
  }
  return render(request, 'app/register_user.html', context)

def update_user(request, user_id):
  if not request.user.is_authenticated:
    return render(request, 'app/login.html')
  user_model = get_user_model()
  user = get_object_or_404(user_model, pk=user_id)
  form = UpdateUserForm(request.POST or None, instance=user)
  if form.is_valid():
    user = form.save(commit=False)
    user.save()
    return render(request, 'app/index.html')
  context = {
    'form': form,
  }
  return render(request, 'app/profile.html', context)

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
  return render(request, 'app/login.html')