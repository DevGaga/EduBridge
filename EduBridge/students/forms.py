from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from students.models import StudentProfile

class StudentSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    education_level = forms.ChoiceField(choices=[
        ('high_school', 'High School'),
        ('undergraduate', 'Undergraduate'),
        ('postgraduate', 'Postgraduate'),
        ('other', 'Other'),
    ])
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    year_of_completion = forms.IntegerField()
    supporting_documents = forms.MultipleChoiceField(
        choices=[
            ('cv', 'CV'),
            ('cover_letter', 'Cover Letter'),
            ('resume', 'Resume'),
            ('recommendation_letter', 'Recommendation Letter'),
        ],
        widget=forms.CheckboxSelectMultiple
    )
    document_file = forms.FileField(required=False)
    phone = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.role = 'student'

        if commit:
            user.save()

            # Create related StudentProfile
            StudentProfile.objects.create(
                user=user,
                full_name=f"{self.cleaned_data['first_name']} {self.cleaned_data['last_name']}",
                education_level=self.cleaned_data['education_level'],
                date_of_birth=self.cleaned_data['date_of_birth'],
                year_of_completion=self.cleaned_data['year_of_completion'],
                phone=self.cleaned_data['phone'],
                cv=self.cleaned_data['document_file'],
            )
        return user
