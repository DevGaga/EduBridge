from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    education_level = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)

    def __str__(self):
        return self.full_name
