from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from institutions.models import Institution

class InstitutionSignupForm(UserCreationForm):
    name = forms.CharField(
        max_length=255,
        label="Institution Name",
        widget=forms.TextInput(attrs={'placeholder': 'Institution Name'})
    )

    contact_email = forms.EmailField(
        label="Contact Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Contact Email'})
    )

    website = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'Institution Website'})
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Brief description about the institution'}),
        required=False,
        label="Description"
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

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'institutions'
        user.username = self.cleaned_data['email']

        if commit:
            user.save()

            # Create associated institution profile
            Institution.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                contact_email=self.cleaned_data['contact_email'],
                website=self.cleaned_data.get('website'),
                description=self.cleaned_data.get('description'),
            )

        return user
