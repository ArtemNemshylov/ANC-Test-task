from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_of_employment = models.DateField()
    email = models.EmailField(max_length=255, unique=True)
    chief = models.ForeignKey(
        'self', on_delete=models.SET_NULL(), null=True, blank=True,
        help_text="The chief of the employee. Can be null if not assigned."
    )

    class Meta:
        ordering = ['full_name']
        # added indexes for search optimization
        indexes = [
            models.Index(fields=['position']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.full_name, self.position, self.email
