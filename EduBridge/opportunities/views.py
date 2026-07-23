from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Opportunity


def _filtered_opportunities(request):
    query = request.GET.get('q', '').strip()
    field = request.GET.get('field', '').strip()

    opportunities = Opportunity.objects.select_related('institution').order_by('-created_at')

    if query:
        opportunities = opportunities.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(requirements__icontains=query)
            | Q(location__icontains=query)
            | Q(opportunity_type__icontains=query)
            | Q(field__icontains=query)
            | Q(institution__name__icontains=query)
        )

    if field:
        opportunities = opportunities.filter(field=field)

    return opportunities


def public_list(request):
    opportunities = _filtered_opportunities(request)
    return render(request, 'opportunities/opportunities.html', {
        'opportunities': opportunities,
        'query': request.GET.get('q', '').strip(),
        'selected_field': request.GET.get('field', '').strip(),
        'field_choices': Opportunity.FIELD_CHOICES,
    })


def detail(request, pk):
    opportunity = get_object_or_404(Opportunity.objects.select_related('institution'), pk=pk)
    return render(request, 'opportunities/detail.html', {
        'opportunity': opportunity,
    })
