from django.urls import re_path
from . import views

app_name = 'app'

urlpatterns = [
  re_path(r'^$', views.index, name='home'),
  re_path(r'^login/$', views.login_view, name='login_view'),
  re_path(r'^register-user/$', views.register, name='register_user'),
  re_path(r'^patients/$', views.patient_list, name='patient_list'),
]
