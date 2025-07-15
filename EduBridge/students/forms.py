from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from students.models import StudentProfile

class StudentSignupForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )

    education_level = forms.ChoiceField(
        choices=[
            ('high_school', 'High School'),
            ('undergraduate', 'Undergraduate'),
            ('postgraduate', 'Postgraduate'),
            ('other', 'Other'),
        ],
        widget=forms.Select()
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    year_of_completion = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'e.g. 2024'})
    )

    supporting_documents = forms.MultipleChoiceField(
        choices=[
            ('cv', 'CV'),
            ('cover_letter', 'Cover Letter'),
            ('resume', 'Resume'),
            ('recommendation_letter', 'Recommendation Letter'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    document_file = forms.FileField(
        required=False,
        help_text="Upload a CV or other document"
    )

    phone = forms.CharField(
        max_length=15, 
        widget=forms.TextInput(attrs={'placeholder': 'Phone number'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.role = 'student'

        if commit:
            user.save()

            # Save StudentProfile
            StudentProfile.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                education_level=self.cleaned_data['education_level'],
                date_of_birth=self.cleaned_data['date_of_birth'],
                year_of_completion=self.cleaned_data['year_of_completion'],
                phone=self.cleaned_data['phone'],
                cv=self.cleaned_data.get('document_file'),  # Optional file
                supporting_documents=self.cleaned_data.get('supporting_documents', [])
            )

        return user
