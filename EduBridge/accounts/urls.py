from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    # Combined account landing page
    path('create_account/', views.CustomLoginView.as_view(), name='create_account'),

    # Login
    path('institution/login/', views.InstitutionLoginView.as_view(), name='institution_login'),
    path('student/login/', views.StudentLoginView.as_view(), name='student_login'),

    # Registration
    path('institution/register/', views.InstitutionRegisterView.as_view(), name='register_institution'),
    path('student/register/', views.StudentRegisterView.as_view(), name='student_signup'),

    # Dashboard redirection
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),

    # Logout
    path('logout/', LogoutView.as_view(next_page='accounts:create_account'), name='logout'),
]
