from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
    path('ajax/validate_employee_code/', views.validate_employee_code, name='validate_employee_code'),
    # path('holidays', views.holidays, name='holidays'),
    path('a_attendance', views.admin_attendance, name='a_attendance'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('add_project', views.add_project, name='add_project'),
    path('add_project_task/', views.add_project_task, name='add_project_task'),
]
