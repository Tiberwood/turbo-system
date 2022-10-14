from django.urls import re_path
from . import views

app_name = 'app'

urlpatterns = [
  re_path(r'^$', views.index, name='home'),
  re_path(r'^login/$', views.login_view, name='login_view'),
  re_path(r'^logout/$', views.logout_view, name='logout_view'),
  re_path(r'^register-user/$', views.register, name='register_user'),
  re_path(r'^register/$', views.register_account, name='register_account'),
  re_path(r'^patients/$', views.patient_list, name='patient_list'),
  re_path(r'^doctors/$', views.doctor_list, name='doctor_list'),
  re_path(r'^(?P<user_id>[0-9]+)/profile/$', views.update_user, name='profile'),
]
