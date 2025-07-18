from django.db import models
from institutions.models import Institution

class Opportunity(models.Model):
    TYPE_CHOICES = [
        ('scholarship', 'Scholarship'),
        ('internship', 'Internship'),
        ('grant', 'Grant')
    ]

    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    opportunity_type = models.CharField(max_length=20, choices=TYPE_CHOICES)  # changed here
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.opportunity_type})"
