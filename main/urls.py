from django.urls import path

from main import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('dashboard', views.admin_dashboard, name='a_dashboard'),
]
