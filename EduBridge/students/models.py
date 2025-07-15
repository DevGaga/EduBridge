from django.db import models
from accounts.models import User
import datetime

class StudentProfile(models.Model):
    EDUCATION_LEVEL_CHOICES = [
        ('high_school', 'High School'),
        ('diploma', 'Diploma'),
        ('bachelor', 'Bachelor’s Degree'),
        ('masters', 'Master’s Degree'),
        ('phd', 'PhD'),
    ]

    DOCUMENT_TYPE_CHOICES = [
        ('cv', 'Curriculum Vitae'),
        ('cover_letter', 'Cover Letter'),
        ('resume', 'Resume'),
        ('recommendation', 'Recommendation Letter'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100, default='John')
    last_name = models.CharField(max_length=100, default='Doe')
    education_level = models.CharField(
        max_length=50,
        choices=EDUCATION_LEVEL_CHOICES,
        default='high_school'
    )
    date_of_birth = models.DateField(default=datetime.date(2000, 1, 1))
    year_of_completion = models.PositiveIntegerField(default=2020)

    supporting_documents = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPE_CHOICES,
        default='cv',
        help_text="Select the type of document being uploaded"
    )
    document_file = models.FileField(upload_to='documents/', null=True, blank=True)

    phone = models.CharField(max_length=15, default='0000000000')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
                            