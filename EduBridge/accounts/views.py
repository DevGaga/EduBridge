from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView
from .models import User
from .forms import StudentSignupForm, InstitutionSignupForm

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'accounts/created_account.html'  # Fixed typo: was 'create_account.html'

# Role-Based Dashboard Redirect
@login_required
def dashboard_redirect(request):
    if request.user.role == 'student':
        return redirect('students:dashboard')
    elif request.user.role == 'institutions':
        return redirect('institutions:dashboard')
    else:
        return redirect('admin:index')  # default for superusers/admin

# Student Signup View
class StudentRegisterView(CreateView):
    model = User
    form_class = StudentSignupForm
    template_name = 'accounts/student_signup.html'  # Correct template

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:dashboard')

# Institution Signup View
class InstitutionRegisterView(CreateView):
    model = User
    form_class = InstitutionSignupForm
    template_name = 'accounts/register_institution.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('institutions:dashboard')
