from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Application

@login_required
def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk)
    return render(request, 'applications/detail.html', {
        'application': application
    })
