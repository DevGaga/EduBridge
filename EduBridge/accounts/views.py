from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView
from .models import User
from .forms import StudentSignupForm, InstitutionSignupForm

# Login view (you can customize template)
class CustomLoginView(LoginView):
    template_name = 'accounts/create_account.html'

# Redirect user based on role
@login_required
def dashboard_redirect(request):
    if request.user.role == 'students':
        return redirect('students:dashboard')
    elif request.user.role == 'institutions':
        return redirect('institutions:dashboard')
    else:
        return redirect('admin:index')

# Student registration
class StudentRegisterView(CreateView):
    model = User
    form_class = StudentSignupForm
    template_name = 'accounts/.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:dashboard')

# Institution registration
class InstitutionRegisterView(CreateView):
    model = User
    form_class = InstitutionSignupForm
    template_name = 'accounts/register_institution.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('institutions:dashboard')
