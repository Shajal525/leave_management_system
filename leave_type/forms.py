from django import forms
from .models import LeaveModel
from django.utils.translation import ugettext_lazy as _


class LeaveForm(forms.ModelForm):

    class Meta:
        model = LeaveModel
        fields = ('leave_type', 'leave_criteria', 'leave_number_of_months', 'leave_months_per_year', 'leave_salary_type', 'leave_depands_on_working_days')

    def clean_leave_type(self):
        type = self.cleaned_data['leave_type']
        return type[0].upper()+type[1:].lower()

    def clean(self):
        cleaned_data = super().clean()
        if self.is_valid():
            return cleaned_data
        else:
            raise forms.ValidationError(_('Invalid content'))

class LeaveUpdateForm(forms.ModelForm):

    class Meta:
        model = LeaveModel
        fields = ('leave_type', 'leave_criteria',  'leave_number_of_months', 'leave_months_per_year', 'leave_salary_type', 'leave_depands_on_working_days')

    def clean_leave_type(self):
        type = self.cleaned_data['leave_type']
        return type[0].upper()+type[1:].lower()

    def clean(self):
        cleaned_data = super().clean()
        if self.is_valid():
            return cleaned_data
        else:
            raise forms.ValidationError(_('Invalid content'))
