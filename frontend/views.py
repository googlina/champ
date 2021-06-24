from django.shortcuts import render
from backend.forms import AddDepartmentForm, AddDesignationForm, Add_Employee_Form,AddProjectForm
from backend.models import Department,Designation,Employee,Depot,User_type,Project,FamilyInfo,WorkExpInfo,EduInfo
import os
from champ.settings import BASE_DIR
# Create your views here.


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from main.models import CustomUser


def user_login(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(id=request.user.id)
        print(user)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'Admin':
                return redirect('a_dashboard')
            elif user.user_type == 'Employee':
                return redirect('e_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def employee_dashboard(request):
    return render(request, 'e_dashboard.html')



def employee_profile(request,pk):
    employee = Employee.objects.get(id=pk)
    family_info = FamilyInfo.objects.filter(employee__employee_id=pk)
    work_info = WorkExpInfo.objects.filter(employee__employee_id=pk)
    edu_info = EduInfo.objects.filter(employee__employee_id = pk)
    projects = Project.objects.prefetch_related()
    emp_projects = []
    for project in projects:
        for emp in project.assigned_to.all():
            if emp.id == employee.id or project.assigned_by_id == employee.id:
                emp_projects.append(project)
    context = {'employee':employee,'family_info':family_info,'work_info':work_info,'edu_info':edu_info,'emp_projects':emp_projects}
    return render(request,'employee_profile.html',context)

def e_list(request):
    form = Add_Employee_Form
    departments = Department.objects.prefetch_related()
    designations = Designation.objects.prefetch_related()
    depots = Depot.objects.prefetch_related()
    employees = Employee.objects.prefetch_related()
    user_types = User_type.objects.prefetch_related()
    context = {'form': form, 'departments': departments,'designations':designations,'depots':depots,'employess':employees,'user_types':user_types}
    return render(request, 'employee_list.html', context)


def e_grid(request):
    return render(request,'e_list_grid.html')


def e_project(request):
    form = AddProjectForm

    projects = Project.objects.order_by('-id')[:8]
    context = {'form': form,'projects':projects}
    return render(request, 'e_project.html',context)


def view_project(request,pk):
    project = Project.objects.get(id=pk)
    my_list = (project.files.name).split('/',-1)
    project_file_name = my_list[-1]
    context = {'project': project,'project_file_name':project_file_name}
    return render(request,'view_project.html',context)

def departments(request):
    form = AddDepartmentForm
    departments = Department.objects.prefetch_related().all()
    context = {'form':form,'departments':departments}
    return render(request, 'departments.html',context)    


def designations(request):
    form = AddDesignationForm
    designations = Designation.objects.select_related('department').prefetch_related().all()
    context = {'form':form,'designations':designations}
    return render(request, 'designations.html',context)        

def e_task(request):
    form = AddProjectForm
    projects = Project.objects.order_by('-id')
    context = {'projects': projects,'form':form}
    return render(request, 'e_task.html',context)


def view_task(request,pk):
    pass

def e_task_board(request):
    return render(request, 'e_task_board.html')


def e_attendance(request):
    return render(request, 'e_attendance.html')


def e_leave(request):
    return render(request, 'e_leave.html')


def e_timesheet(request):
    return render(request, 'e_timesheet.html')


def e_holidays(request):
    return render(request, 'e_holidays.html')


def e_payslip(request):
    return render(request, 'e_payslip.html')


def e_leads(request):
    return render(request, 'e_lead.html')


def e_ticket(request):
    return render(request, 'e_tickets.html')



def e_policy(request):
    return render(request, 'e_policy.html')



def e_training(request):
    return render(request,'e_training.html')


def e_resignation(request):
    return render(request,'e_resignation.html')


def e_jobs(request):
    return render(request,'e_jobs.html')


def knowledge_base(request):
    return render(request,'knowledge_base.html')


def e_activity(request):
    return render(request,'e_activity.html')