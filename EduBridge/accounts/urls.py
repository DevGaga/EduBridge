# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('create-account/', views.CustomLoginView.as_view(), name='create_account'),
    path('student-login/', views.StudentLoginView.as_view(), name='student_login'),
    path('institution-login/', views.InstitutionLoginView.as_view(), name='institution_login'),
    path('student-signup/', views.StudentRegisterView.as_view(), name='student_signup'),
    path('register-institution/', views.InstitutionRegisterView.as_view(), name='register_institution'),
    
    # 🔁 Redirect logic here:
    path('redirect-dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
]
