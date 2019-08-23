from django.db import models
from users.models import CustomUser

# Create your models here.

class LeaveModel(models.Model):
    LEAVE_CHOICES = [
            ('FULL', 'Full'),
            ('HALF', 'Half'),
            ('NO', 'No')
    ]
    leave_type = models.CharField(max_length=250, blank=False)
    leave_criteria = models.TextField(blank=False)
    leave_number_of_months = models.PositiveIntegerField(default=1, blank=False)
    leave_months_per_year = models.PositiveIntegerField(default=1, blank=False)
    leave_salary_type = models.CharField(max_length=250, choices=LEAVE_CHOICES, default='FULL', blank=False)
    leave_depands_on_working_days = models.BooleanField(default=False)


    def __str__(self):
        return self.leave_type

    def leave_number_of_days(self):
        return self.leave_number_of_months * 30
