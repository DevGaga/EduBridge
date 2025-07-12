from django import forms
from .models import Opportunity

class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = [
            'institution',
            'title',
            'opportunity_type',  # This must match the model exactly
            'description',
            'requirements',
            'location',
            'deadline'
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'requirements': forms.Textarea(attrs={'rows': 3}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'opportunity_type': 'Type of Opportunity',
        }
