from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ApplicationForm
from .models import ApplicationModel
from leave_type.models import LeaveModel
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import ensure_csrf_cookie
from datetime  import date, timedelta
from django import forms
from django.utils.translation import ugettext_lazy as _

# Create your views here.

@login_required(login_url='home')
@ensure_csrf_cookie
def applyView(request):
    leaves = LeaveModel.objects.all()
    if request.method == 'POST':
        form = ApplicationForm(data=request.POST, user=request.user)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.leave_type = get_object_or_404(LeaveModel, id=request.POST.get('leave_type'))
            if request.FILES.get('attachment') is not None:
                application.attachment = request.FILES.get('attachment')

            application.save()
            messages.success(request, 'Your application submited.')
            return redirect('/applications/'+str(application.id))
        else:
            messages.error(request, 'Please correct the error!!.')
            return render(request, 'applications/staff/apply_for_leave.html', {'form':form, 'leaves':leaves})
    else:
        form = ApplicationForm(user=request.user)
        return render(request, 'applications/staff/apply_for_leave.html', {'form':form, 'leaves':leaves})


@login_required(login_url='home')
@ensure_csrf_cookie
def DetailView(request, ap_id):
    application = get_object_or_404(ApplicationModel, pk=ap_id)
    return render(request, 'applications/detail.html', {'application':application})


@login_required(login_url='home')
@ensure_csrf_cookie
def allView(request):
    all_applications = ApplicationModel.objects.all()
    if request.user.is_staff:
        return render(request, 'applications/all_application.html', {'all_applications':all_applications})
    else:
        user_applications = []
        for ap in all_applications:
            if ap.applicant == request.user:
                user_applications.append(ap)
        return render(request, 'applications/all_application.html', {'all_applications':user_applications})


@staff_member_required(login_url='home')
@ensure_csrf_cookie
def leaveApproveOrDenayView(request, ap_id, approve):
    application = get_object_or_404(ApplicationModel, pk=ap_id)
    if application.status == 'PANDING':
        application.status = 'APPROVED' if approve == 1 else 'DENAYED'
        if approve == 1:
            application.applicant.on_leave_till = application.leave_end_date
            application.applicant.save()
        application.save()
    return redirect('applications:detail', ap_id=ap_id)
