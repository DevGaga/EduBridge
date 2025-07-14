from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Institution Signup Form
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

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'institutions'
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
            # Create related InstitutionProfile if it exists
            try:
                from institutions.models import InstitutionProfile
                InstitutionProfile.objects.create(
                    user=user,
                    name=self.cleaned_data['name'],
                    type=self.cleaned_data['type']
                )
            except ImportError:
                pass
        return user


# Student Signup Form
class StudentSignupForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        label="First Name",
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=100,
        label="Last Name",
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
            # Create related StudentProfile if it exists
            try:
                from students.models import StudentProfile
                StudentProfile.objects.create(
                    user=user,
                    first_name=self.cleaned_data['first_name'],
                    last_name=self.cleaned_data['last_name']
                )
            except ImportError:
                pass
        return user
