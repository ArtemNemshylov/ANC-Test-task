from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_of_employment = models.DateField()
    email = models.EmailField(unique=True)
    level = models.IntegerField()
    chief = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='subordinates')

    class Meta:
        ordering = ['full_name']
        # added indexes for search optimization
        indexes = [
            models.Index(fields=['position']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.full_name
