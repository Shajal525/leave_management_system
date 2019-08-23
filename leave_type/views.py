from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import LeaveForm
from .models import LeaveModel
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

@login_required(login_url='home')
@ensure_csrf_cookie
def allView(request):
    leaves = LeaveModel.objects
    return render(request, 'leave_type/all_leave_types.html', {'leaves':leaves})


@staff_member_required(login_url='home')
@ensure_csrf_cookie
def createView(request):
    if request.method == 'POST':
        form = LeaveForm(data=request.POST)
        if form.is_valid():
            leave = form.save()
            messages.success(request, 'Leave type created.')
            return redirect('/leave_types/detail/'+str(leave.id))
        else:
            messages.error(request, 'Please correct the error!!.')
            return render(request, 'leave_type/create_leave.html', {'form':form})
    else:
        form = LeaveForm()
        return render(request, 'leave_type/create_leave.html', {'form':form})

@staff_member_required(login_url='home')
@ensure_csrf_cookie
def updateView(request, lv_id):
    selected = get_object_or_404(LeaveModel, id=lv_id)
    if request.method == 'POST':
        form = LeaveForm(data=request.POST, instance=selected)
        if form.is_valid():
            leave = form.save()
            messages.success(request, 'Leave type created.')
            return redirect('/leave_types/detail/'+str(leave.id))
        else:
            messages.error(request, 'Please correct the error!!.')
            return render(request, 'leave_type/update_leave.html', {'form':form})
    else:
        form = LeaveForm(instance=selected)
        return render(request, 'leave_type/update_leave.html', {'form':form})


@login_required(login_url='home')
@ensure_csrf_cookie
def detailView(request, lv_id):
    leave = get_object_or_404(LeaveModel, pk=lv_id)
    return render(request, 'leave_type/leave_detail.html', {'leave':leave})

@staff_member_required(login_url='home')
@ensure_csrf_cookie
def deleteView(request, lv_id):
    leave = get_object_or_404(LeaveModel, pk=lv_id)
    leave.delete()
    return redirect('leave_types:leave_types')
