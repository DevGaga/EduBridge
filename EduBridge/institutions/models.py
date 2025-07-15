from django.db import models
from accounts.models import User

class Institution(models.Model):
    INSTITUTION_TYPES = [
        ('university', 'University'),
        ('college', 'College'),
        ('company', 'Company'),
        ('ngo', 'NGO'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=50,
        choices=INSTITUTION_TYPES,
        default='university'  # ✅ Default added here to fix makemigrations issue
    )
    contact_email = models.EmailField()
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
