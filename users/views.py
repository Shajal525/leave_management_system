from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import auth
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from users.models import CustomUser
from datetime  import date, timedelta
from django.utils import timezone
from leave_type.models import LeaveModel

# Create your views here.

def homeView(request):
    return render(request, 'users/home.html')

@ensure_csrf_cookie
def loginView(request, admin):
    error = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user:
            if user.is_active and user.is_staff and user.is_superuser and admin == 1:
                auth.login(request, user)
                return redirect('home')
            if user.is_active and admin == 0 and not user.is_staff and not user.is_superuser:
                auth.login(request, user)
                return redirect('home')
            else:
                error = "Not found! Make sure you are in staff or admin page."
                return render(request, 'users/login.html', { 'admin':admin, 'error':error })
        else:
            error = "Email and password didn't match!"
            return render(request, 'users/login.html', { 'admin':admin, 'error':error })
    else:
        return render(request, 'users/login.html', { 'admin':admin, 'error':error })

@login_required(login_url='home')
def logoutView(request):
    auth.logout(request)
    return redirect('home')

@staff_member_required(login_url='home')
@ensure_csrf_cookie
def createUserView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.on_leave_till = user.on_leave_till - timedelta(days = 1)
            user.save()
            return redirect('/users/'+str(user.id))
        else:
            return render(request, 'users/admin/create_user.html', {'form':form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'users/admin/create_user.html', {'form':form})

@login_required(login_url='home')
def userDetailView(request, id):
    if request.user.is_staff:
        selected = get_object_or_404(CustomUser, pk=id)
        return render(request, 'users/user_detail.html', {'selected_user':selected})
    else:
        selected = get_object_or_404(CustomUser, pk=request.user.id)
        #status = user_application_status(request.user)
        return render(request, 'users/user_detail.html', {'selected_user':selected})

@ensure_csrf_cookie
@staff_member_required(login_url='home')
def deleteUserView(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    user.delete()
    return redirect('home')

@ensure_csrf_cookie
@login_required(login_url='home')
def updateUserView(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            if request.FILES.get('image') is not None:
                user.image = request.FILES.get('image')
            user.save()
            return redirect('home')
        else:
            return render(request, 'users/update_info.html', {'form':form})
    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'users/update_info.html', {'form':form})

@ensure_csrf_cookie
@login_required(login_url='home')
def passwordChangeView(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully changed.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error!!.')
            return render(request, 'users/password_change.html', {'form':form})
    else:
        form = CustomPasswordChangeForm(user=request.user)
        return render(request, 'users/password_change.html', {'form':form})

def aboutView(request):
    return render(request, 'about.html')

def helpView(request):
    return render(request, 'help.html')
