from django.urls import path,include
from users import views


urlpatterns = [
    path('', views.homeView, name='home'),
    path('login/<int:admin>', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('create_user/', views.createUserView, name='create_user'),
    path('delete_user/<int:id>', views.deleteUserView, name='delete_user'),
    path('update_info/', views.updateUserView, name='update_info'),
    path('password/', views.passwordChangeView, name='password'),
    path('users/<int:id>', views.userDetailView, name='user_detail'),
    path('applications/', include('applications.urls')),
    path('leave_types/', include('leave_type.urls')),

]
