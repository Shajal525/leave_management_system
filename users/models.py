from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime  import datetime, timedelta, date

from users.managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=250, blank=False)
    last_name = models.CharField(_('last name'), max_length=250, blank=False)
    image = models.ImageField(upload_to='profile_pic', blank=True)
    bio = models.TextField(_('Bio'), blank=True)
    time = models.DateField(auto_now=True)
    on_leave_till = models.DateField(auto_now_add=True, editable=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return self.first_name+' '+self.last_name

    def accepted_applications(self):
        from applications.models import ApplicationModel
        accepted = []
        leave_appli = ApplicationModel.objects.filter(applicant=self)
        for apl in leave_appli:
            if apl.status == 'APPROVED':
                accepted.append(apl)
        return accepted

    def rejected_applications(self):
        from applications.models import ApplicationModel
        rejected = []
        leave_appli = ApplicationModel.objects.filter(applicant=self)
        for apl in leave_appli:
            if apl.status == 'DENAYED':
                rejected.append(apl)
        return  rejected

    def panding_applications(self):
        from applications.models import ApplicationModel
        panding = []
        leave_appli = ApplicationModel.objects.filter(applicant=self)
        for apl in leave_appli:
            if apl.status == 'PANDING':
                panding.append(apl)
        return panding
