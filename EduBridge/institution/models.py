from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

class Institution(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    website = models.URLField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
