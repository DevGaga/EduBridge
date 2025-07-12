from django import forms
from students.models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'date_of_birth', 'university', 'cv']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }
