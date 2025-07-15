from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from opportunities.models import Opportunity
from applications.models import Application
from .models import StudentProfile
from django.utils.timezone import now

@login_required
def dashboard(request):
    profile = get_object_or_404(StudentProfile, user=request.user)
    applications = Application.objects.filter(student=profile)
    return render(request, 'students/dashboard.html', {
        'profile': profile,
        'applications': applications,
    })

@login_required
def opportunity_list(request):
    opportunities = Opportunity.objects.filter(deadline__gte=now().date()).order_by('-created_at')
    return render(request, 'students/opportunities.html', {
        'opportunities': opportunities,
    })

@login_required
def apply_to_opportunity(request, opportunity_id):
    opportunity = get_object_or_404(Opportunity, id=opportunity_id)
    profile = get_object_or_404(StudentProfile, user=request.user)

    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter')
        Application.objects.create(
            student=profile,
            opportunity=opportunity,
            cover_letter=cover_letter,
        )
        return redirect('students:dashboard')

    return render(request, 'students/apply.html', {
        'opportunity': opportunity
    })
