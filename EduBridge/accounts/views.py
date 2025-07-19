from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse

from .models import User
from .forms import StudentSignupForm, InstitutionSignupForm
from students.models import StudentProfile
from institutions.models import Institution  # if using Institution model


# Account selection page
class CustomLoginView(LoginView):
    template_name = 'accounts/create_account.html'


# Login views
class InstitutionLoginView(LoginView):
    template_name = 'accounts/institution_login.html'

    def get_success_url(self):
        return reverse('accounts:dashboard_redirect')


class StudentLoginView(LoginView):
    template_name = 'accounts/student_login.html'

    def get_success_url(self):
        return reverse('accounts:dashboard_redirect')


# Redirect to correct dashboard based on role
@login_required
def dashboard_redirect(request):
    if request.user.role == 'student':
        return redirect('students:student_dashboard')
    elif request.user.role == 'institutions':
        return redirect('institutions:institution_dashboard')
    else:
        return redirect('admin:index')


# Student signup view
class StudentRegisterView(CreateView):
    model = User
    form_class = StudentSignupForm
    template_name = 'accounts/student_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:dashboard_redirect')


# Institution signup view
class InstitutionRegisterView(CreateView):
    model = User
    form_class = InstitutionSignupForm
    template_name = 'accounts/register_institution.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:dashboard_redirect')
