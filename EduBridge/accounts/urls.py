from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    # Login & logout
    path('create_account/', views.CustomLoginView.as_view(), name='create_account'),
    path('logout/', LogoutView.as_view(next_page='accounts:create_account'), name='logout'),

    # Registration for students and institutions
    path('student/', views.StudentRegisterView.as_view(), name='register_student'),
    path('/institution/', views.InstitutionRegisterView.as_view(), name='register_institution'),

    # Redirect users to their dashboards based on role
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
]
