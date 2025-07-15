from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from students.models import StudentProfile

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
            try:
                from institutions.models import Institution
                Institution.objects.create(
                    user=user,
                    name=self.cleaned_data['name'],
                    contact_email=user.email,
                    description="",
                    website=""
                )
            except ImportError:
                pass
        return user


# Student Signup Form
class StudentSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    education_level = forms.ChoiceField(choices=[
        ('high_school', 'High School'),
        ('diploma', 'Diploma'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD'),
    ])
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    year_of_completion = forms.IntegerField()
    supporting_documents = forms.MultipleChoiceField(
        choices=[
            ('cv', 'CV'),
            ('cover_letter', 'Cover Letter'),
            ('resume', 'Resume'),
            ('recommendation', 'Recommendation Letter'),
        ],
        widget=forms.CheckboxSelectMultiple
    )
    phone = forms.CharField(max_length=15)
    cv = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            StudentProfile.objects.create(
                user=user,
                full_name=f"{user.first_name} {user.last_name}",
                education_level=self.cleaned_data['education_level'],
                date_of_birth=self.cleaned_data['date_of_birth'],
                year_of_completion=self.cleaned_data['year_of_completion'],
                supporting_documents=self.cleaned_data['supporting_documents'],
                phone=self.cleaned_data['phone'],
                email=user.email,
                cv=self.cleaned_data.get('cv')
            )
        return user
