from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from backend.models import Department, Employee, Designation, User_type, Project
from main.models import CustomUser

# Create your views here.
from backend.forms import Add_Employee_Form, AddProjectForm


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def validate_employee_code(request):
    employee_code = request.GET.get('employee_code', None)
    print(f'Employee code is {employee_code}')
    data = {
        'is_taken': Employee.objects.filter(code__iexact=employee_code).exists()
    }
    return JsonResponse(data)


def add_employee(request):
    try:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user_name = request.POST['username']
            email = request.POST['email']
            contact = request.POST['contact']
            employee_code = request.POST['employee_code']
            birthday = request.POST['birthday']
            joining_date = request.POST['joining_date']
            department = request.POST['department']
            designation = request.POST['designation']
            superwiser = request.POST['superwiser']
            location = request.POST['location']
            user_type = request.POST['user_type']
            # Fetching department id from database and that id will be assigned to new employee
            department_id = Department.objects.get(id=department)
            department_id = department_id.id
            # Fetching designation id from database and that id will be assigned to new employee
            designation_id = Designation.objects.get(id=designation)
            designation_id = designation_id.id
            # Fetching user_type id from database and that id will be assigned to new employee
            user_type = User_type.objects.get(id=user_type)
            user_type = user_type.user_type
            # Checking if entered username already exists in database or not
            if CustomUser.objects.filter(username__iexact=user_name).exists():
                messages.error(request, 'User with this username already exist')
            # Checking if entered employee code already exists in database or not
            elif Employee.objects.filter(code__iexact=employee_code).exists():
                messages.error(request, 'User with this frontend code already exists')
            else:
                # Creating new user for before adding new frontend this user will be assigned to created employee
                user = get_user_model().objects.create(username=user_name, first_name=first_name, last_name=last_name,
                                                       user_type=user_type)
                # Setting password for new created user. contact number is their password
                user.set_password(contact)
                user.save()
                # Creating new employee
                new_employee = Employee.objects.create(code=employee_code, first_name=first_name, last_name=last_name,
                                                       contact=contact, email=email, department_id=department_id,
                                                       designation_id=designation_id, work_location_id=location,
                                                       superwiser_id=superwiser, joining_date=joining_date,
                                                       birthday=birthday, employee=user)
                # Saving new employee
                new_employee.save()
                messages.success(request, 'Employee added successfully')
                return redirect('e_list')
    except Exception as e:
        messages.error(request, f'Something went wrong, Error code is {e}')
    return redirect('e_list')


def add_project(request):
    if request.method == 'POST':
        project_name = request.POST['name']
        department = request.POST['department']
        start_date = request.POST['start_date']
        deadline = request.POST['deadline']
        priority = request.POST['priority']
        leader = request.POST['leader']
        assigned_to = request.POST['assigned_to']
        description = request.POST['description']
        file = request.FILES.get('file')
        print(
            f'Project name is {project_name}, department is {department}, start date is {start_date}, deadline is {deadline}, priority is {priority}, leader is {leader}, team members are {assigned_to}, description is {description}')
        newProject = Project.objects.create(name=project_name, department_id=department, start_date=start_date,
                                            deadline=deadline, priority=priority, leader_id=leader,
                                            description=description, files=file, created_by_id=request.user.id)
        newProject.save()
        newProject.assigned_to.set(assigned_to)
        newProject.save()
        messages.success(request, 'Project has been created. Now you add tasks to this project')
        print('Project has been added')
    return redirect('e_project')


def add_project_task(request):
    if request.method == "POST":
        project_id = request.POST['pid']
        task_name = request.POST['task_name']
        task_description = request.POST['task_description']
        task_file = request.POST['task_file']
        print(project_id,task_name,task_description,task_file)
    return JsonResponse('')


def admin_attendance(request):
    return render(request, 'admin/attendance_admin.html')


def holidays(request):
    return render(request, 'e_holidays.html')
