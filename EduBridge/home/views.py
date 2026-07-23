from django.db.models import Q
from django.shortcuts import render

from opportunities.models import Opportunity

def index(request):
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

    return render(request, 'home/index.html', {
        'opportunities': opportunities[:6],
        'query': query,
        'selected_field': field,
        'field_choices': Opportunity.FIELD_CHOICES,
    })
