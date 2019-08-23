from django import forms
from django.forms import widgets
from .models import ApplicationModel
from leave_type.models import LeaveModel
from django.utils.translation import ugettext_lazy as _
from datetime  import date
from django.shortcuts import get_object_or_404



class ApplicationForm(forms.ModelForm):
    leave_start_date = forms.DateField(widget=widgets.SelectDateWidget(), initial=date.today)
    leave_end_date = forms.DateField(widget=widgets.SelectDateWidget(), initial=date.today)

    class Meta:
        model = ApplicationModel
        fields = ('title', 'leave_type', 'body', 'leave_start_date', 'leave_end_date', 'attachment')

    def clean_title(self):
        titlee = self.cleaned_data['title']
        return titlee[0].upper()+titlee[1:].lower()

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('leave_start_date')
        end_date = cleaned_data.get('leave_end_date')

        if start_date < date.today()  or end_date < start_date:
            raise forms.ValidationError(_('Date invalid!'), code='invalid')
        else:
            if self.is_valid():
                return_msg = all_good(cleaned_data, self.user)
                if return_msg == "true":
                    return cleaned_data
                else:
                    raise forms.ValidationError(_(return_msg), code='invalid')
            else:
                raise forms.ValidationError(_('Invalid Data Provided!'), code='invalid')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)


def all_good(cleaned_f, userr):
    if cleaned_f.get('leave_start_date') <= userr.on_leave_till:
        return "You are already on leave till " + str(userr.on_leave_till) + "."
    leave_typee = cleaned_f.get('leave_type')
    prev_appli = ApplicationModel.objects.filter(applicant=userr, status='APPROVED', leave_type=leave_typee)

    leave = get_object_or_404(LeaveModel, leave_type=leave_typee)
    prev_leaves = 0
    this_year_leave = 0
    for ap in prev_appli:
        prev_leaves += ap.total_leave()
        if ap.leave_end_date.year == cleaned_f.get('leave_start_date').year:
            this_year_leave += (ap.leave_end_date - date(ap.leave_end_date.year, 1, 1)).days + 1
    available_leaves = leave.leave_number_of_months*30 - prev_leaves
    leave_asked_this_year = (date(cleaned_f.get('leave_start_date').year, 12, 31)-cleaned_f.get('leave_start_date')).days + 1
    leave_asked_next_year = 0
    if cleaned_f.get('leave_start_date').year != cleaned_f.get('leave_end_date').year:
        leave_asked_next_year += (cleaned_f.get('leave_end_date') - date(cleaned_f.get('leave_end_date').year, 1, 1)).days + 1

    leave_asked = (cleaned_f.get('leave_end_date')-cleaned_f.get('leave_start_date')).days + 1
    if available_leaves >= leave_asked:
        per_year = 0
        if cleaned_f.get('leave_end_date').year >= date.today().year:
            per_year = leave.leave_months_per_year*30-this_year_leave
        else:
            per_year = leave.leave_months_per_year*30
        if per_year >= leave_asked_this_year and leave.leave_months_per_year*30 >= leave_asked_next_year:
            if leave.leave_depands_on_working_days == True:
                days_worked = (date.today()-userr.time).days - prev_leaves
                leave_av = int(days_worked/11)
                if leave_av >= leave_asked:
                    return 'true'
                else:
                    return "You need to work more days! Your Leave Available: " + str(leave_av) + " days."
            else:
                return "true"
        else:
            return "Per year leave is lesser! You asked: " + str(leave_asked_this_year) + " days leave this year and " + str(leave_asked_next_year)+ " days leave next year. Available This Year: " + str(per_year)+" days."
    else:
        return str(leave_asked)+" days Leave not available!"
