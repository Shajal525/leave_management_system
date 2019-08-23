from django.urls import path
from leave_type import views

app_name = 'leave_types'

urlpatterns = [
    path('all', views.allView, name='leave_types'),
    path('create_leave', views.createView, name='create_leave'),
    path('detail/<int:lv_id>', views.detailView, name='leave_detail'),
    path('update/<int:lv_id>', views.updateView, name='leave_update'),
    path('delete/<int:lv_id>', views.deleteView, name='leave_delete'),
]
