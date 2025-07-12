from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    # Login & logout
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),

    # Registration for students and institutions
    path('register/student/', views.StudentRegisterView.as_view(), name='register_student'),
    path('register/institution/', views.InstitutionRegisterView.as_view(), name='register_institution'),

    # Redirect users to their dashboards based on role
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
]
