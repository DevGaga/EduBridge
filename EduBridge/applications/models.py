from django.db import models

class Application(models.Model):
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE)
    opportunity = models.ForeignKey('opportunities.Opportunity', on_delete=models.CASCADE)
    cover_letter = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('submitted', 'Submitted'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], default='submitted')

    def __str__(self):
        return f"{self.student.full_name} - {self.opportunity.title}"
