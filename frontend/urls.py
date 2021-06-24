from django.urls import path

from frontend import views

urlpatterns = [
    path('e_dashboard', views.employee_dashboard, name='e_dashboard'),
    path('e_list', views.e_list, name='e_list'),
    path('employee_profile<int:pk>', views.employee_profile, name='employee_profile'),
    path('e_grid', views.e_grid, name='e_grid'),
    path('e_project', views.e_project, name='e_project'),
    path('project_view<int:pk>', views.view_project, name='view_project'),
    path('HR/departments/', views.departments, name='departments'),
    path('HR/designations/', views.designations, name='designations'),
    path('e_task', views.e_task, name='e_task'),
    path('view_task<int:pk>', views.view_task, name='view_task'),
    path('e_task_board', views.e_task_board, name='e_task_bord'),
    path('e_attendance', views.e_attendance, name='e_attendance'),
    path('e_leave', views.e_leave, name='e_leave'),
    path('e_timesheet', views.e_timesheet, name='e_timesheet'),
    path('e_holidays', views.e_holidays, name='e_holidays'),
    path('e_payslip', views.e_payslip, name='e_payslip'),
    path('e_leads', views.e_leads, name='e_leads'),
    path('e_ticket', views.e_ticket, name='e_ticket'),
    path('e_policy', views.e_policy, name='e_policy'),
    path('e_training', views.e_training, name='e_training'),
    path('e_resignation', views.e_resignation, name='e_resignation'),
    path('e_jobs', views.e_jobs, name='e_jobs'),
    path('knowledge_base', views.knowledge_base, name='knowledge_base'),
    path('e_activity', views.e_activity, name='e_activity'), 
    path('', views.user_login, name='login'),
    path('dashboard', views.admin_dashboard, name='a_dashboard'),


]
