from django import forms
from institutions.models import InstitutionProfile

class InstitutionProfileForm(forms.ModelForm):
    class Meta:
        model = InstitutionProfile
        fields = ['name', 'description', 'website', 'logo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3})
        }
