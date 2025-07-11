from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Opportunity

def public_list(request):
    opportunities = Opportunity.objects.all().order_by('-created_at')
    return render(request, 'opportunities/list.html', {
        'opportunities': opportunities,
    })
