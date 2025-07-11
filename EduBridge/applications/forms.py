from django import forms
from applications.models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['opportunity', 'resume', 'cover_letter']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cover_letter'].widget.attrs.update({'rows': 5})
