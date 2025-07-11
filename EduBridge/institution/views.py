from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Institution
from opportunities.models import Opportunity
from opportunities.forms import OpportunityForm

@login_required
def dashboard(request):
    institution = get_object_or_404(Institution, user=request.user)
    opportunities = Opportunity.objects.filter(institution=institution)
    return render(request, 'institutions/dashboard.html', {
        'opportunities': opportunities
    })

@login_required
def create_opportunity(request):
    institution = get_object_or_404(Institution, user=request.user)

    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            opp = form.save(commit=False)
            opp.institution = institution
            opp.save()
            return redirect('institutions:dashboard')
    else:
        form = OpportunityForm()

    return render(request, 'institutions/create_opportunity.html', {
        'form': form
    })
