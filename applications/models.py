from django.db import models
from users.models import CustomUser
from leave_type.models import LeaveModel
from datetime  import datetime, timedelta, date

# Create your models here.

class ApplicationModel(models.Model):
    title = models.CharField(max_length=400, blank=False)
    body = models.TextField(blank=False)
    leave_start_date = models.DateField(default=date.today, blank=False)
    leave_end_date = models.DateField(default=date.today, blank=False)
    STATUS_CHOICES = [ ('APPROVED', 'Approved'), ('DENAYED', 'Denayed'), ('PANDING', 'Panding')]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PANDING')
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveModel, on_delete=models.SET_NULL, blank=False, null=True)
    attachment = models.FileField(upload_to='attachment/', blank=True)

    def __str__(self):
        return self.title

    def total_leave(self):
        return (self.leave_end_date - self.leave_start_date).days + 1
