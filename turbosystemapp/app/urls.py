from django.urls import re_path
from .views.PatientView import patient_list, create_patient, upload_exam, find_patient
from .views.DoctorView import doctor_list, create_diagnostic
from .views.UserView import register, register_account, login_view, update_user, logout_view
from .views.HomeView import index, create_diasese

app_name = 'app'

urlpatterns = [
  re_path(r'^$', index, name='home'),
  re_path(r'^login/$', login_view, name='login_view'),
  re_path(r'^logout/$', logout_view, name='logout_view'),
  re_path(r'^register-user/$', register, name='register_user'),
  re_path(r'^register/$', register_account, name='register_account'),
  re_path(r'^patients/$', patient_list, name='patient_list'),
  re_path(r'^doctors/$', doctor_list, name='doctor_list'),
  re_path(r'^(?P<user_id>[0-9]+)/profile/$', update_user, name='profile'),
  re_path(r'^new-disease/$', create_diasese, name='create_disease'),
  re_path(r'^upload-exams/(?P<diagnostic_id>[0-9]+)/$', upload_exam, name='upload_exam'),
  re_path(r'^register-patient/$', create_patient, name='register_patient'),
  re_path(r'^create-diagnostic/(?P<patient_id>[0-9]+)/$', create_diagnostic, name='create_diagnostic'),
  re_path(r'^find-patient/$', find_patient, name='find_patient'),
]
