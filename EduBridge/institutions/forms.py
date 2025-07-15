from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from institutions.models import Institution  # ✅ Corrected import

class InstitutionSignupForm(UserCreationForm):
    name = forms.CharField(
        max_length=255,
        label="Institution Name",
        widget=forms.TextInput(attrs={'placeholder': 'Institution Name'})
    )
    type = forms.ChoiceField(
        choices=[
            ('university', 'University'),
            ('college', 'College'),
            ('company', 'Company'),
            ('ngo', 'NGO')
        ],
        label="Institution Type"
    )
    contact_email = forms.EmailField(
        required=True,
        label="Contact Email",
        widget=forms.EmailInput(attrs={'placeholder': 'e.g. contact@institution.org'})
    )
    website = forms.URLField(
        required=False,
        label="Website",
        widget=forms.URLInput(attrs={'placeholder': 'https://yourinstitution.com'})
    )
    description = forms.CharField(
        required=False,
        label="Description",
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your institution...'})
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'institutions'
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
            # ✅ Create related Institution instance
            Institution.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                type=self.cleaned_data['type'],
                contact_email=self.cleaned_data['contact_email'],
                website=self.cleaned_data.get('website', ''),
                description=self.cleaned_data.get('description', ''),
            )
        return user
