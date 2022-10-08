from random import choices
from django.db import models
from traitlets import default

# Create your models here.
SITUATION_CHOICES = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Disapproved', 'Disapproved')
)

class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=16)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=50, null=True, choices=SITUATION_CHOICES, default='Pending')
    
    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

    def __str__(self):
        return self.first_name

