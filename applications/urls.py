from django.urls import path, include
from applications import views

app_name = 'applications'

urlpatterns = [
    path('apply', views.applyView, name='apply'),
    path('all', views.allView, name='all_applications'),
    path('<int:ap_id>', views.DetailView, name='detail'),
    path('varify/<int:ap_id><int:approve>', views.leaveApproveOrDenayView, name='approve_or_denay'),
]
