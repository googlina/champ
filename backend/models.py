from django.db import models
from main.models import Depot

# Create your models here.

from main.models import Depot


class Department(models.Model):
    department = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.department


class Designation(models.Model):
    designation = models.CharField(max_length=40, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    created_by = models.CharField(max_length=200)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.designation


class User_type(models.Model):
    user_type = models.CharField(max_length=50)

    def __str__(self):
        return self.user_type


# Employee's personal information
class PersonalInfo(models.Model):
    pan = models.CharField(max_length=11, null=True, blank=True)
    aadhar = models.CharField(max_length=16, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=(('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')),
                              null=True, blank=True)
    nationality = models.CharField(max_length=16, null=True, blank=True)
    religion = models.CharField(max_length=16, null=True, blank=True)
    marital_status = models.CharField(
        choices=(('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Separated', 'Separated')), max_length=16,
        null=True, blank=True)
    children = models.CharField(max_length=16, null=True, blank=True)


# Employee's bank information
class BankInfo(models.Model):
    bank_name = models.CharField(max_length=30, null=True, blank=True)
    account_number = models.CharField(max_length=30, null=True, blank=True)
    ifsc = models.CharField(max_length=11, null=True, blank=True)


# Employee's emergency contact details( pri stands for primary and sec stands for secondary)
class EmergencyContact(models.Model):
    pri_contact_num = models.CharField(max_length=13, null=True, blank=True)  # primary emergency contact number
    pri_contact_name = models.CharField(max_length=30, null=True, blank=True)  # primary emergency contact name
    pri_contact_relation = models.CharField(max_length=30, null=True, blank=True)  # primary emergency contact relation
    sec_contact_name = models.CharField(max_length=30, null=True, blank=True)  # secondary emergency contact number
    sec_contact_num = models.CharField(max_length=30, null=True, blank=True)  # primary emergency contact name
    sec_contact_relation = models.CharField(max_length=30, null=True, blank=True)  # primary emergency contact number


class Employee(models.Model):
    employee = models.OneToOneField('main.CustomUser', on_delete=models.CASCADE, related_name='+')
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    bank_info = models.ForeignKey(BankInfo, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    emergency_contact = models.ForeignKey(EmergencyContact, on_delete=models.SET_NULL, null=True, blank=True,
                                          related_name='+')
    code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    profile_image = models.ImageField(upload_to='employee/profile_pic', default='avatar.jpeg', null=True, blank=True)
    work_location = models.ForeignKey(Depot, on_delete=models.SET_NULL, null=True)
    superwiser = models.ForeignKey('backend.Employee', on_delete=models.SET_NULL, null=True, related_name='+',
                                   blank=True)
    joining_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=(('Left', 'Left'), ('Active', 'Active')), default='Active', max_length=30)
    birthday = models.DateField(null=True, blank=True)
    separation_date = models.DateField(blank=True, null=True)
    user_type = models.ForeignKey(User_type, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + self.last_name + ' : ' + self.code


# Employee's educational info
class EduInfo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+', null=True)
    college = models.CharField(max_length=100, null=True, blank=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    marks = models.CharField(max_length=10, blank=True, null=True)


# Employee's work experience information
class WorkExpInfo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    company = models.CharField(max_length=100, null=True, blank=True)  # company worked for
    designation = models.CharField(max_length=50, null=True, blank=True)  # Designation in previous company
    from_date = models.DateField(null=True, blank=True)  # Work from date
    end_date = models.DateField(null=True, blank=True)  # Work to date


# Employee's family information
class FamilyInfo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    name = models.CharField(max_length=13, null=True, blank=True)  # primary contact number
    relation = models.CharField(max_length=30, null=True, blank=True)  # relation with employee
    dob = models.DateField(max_length=30, null=True, blank=True)  # Date of birth of employee's relative
    contact = models.CharField(max_length=15, null=True, blank=True)  # contact number of employee's relative


class Project(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=500)
    start_date = models.DateField(null=True)
    deadline = models.DateField(null=True, blank=True)
    assigned_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='+')
    assigned_to = models.ManyToManyField(Employee, related_name='+')
    leader = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='+')
    priority = models.CharField(choices=(('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')), max_length=100)
    files = models.FileField(upload_to='project_files/% Y/% m/% d/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        choices=(('Pending', 'Pending'), ('In progress', 'In progress'), ('Completed', 'Completed')), max_length=100,
        default='Pending')
    completed_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL)
    task = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    assigned_to = models.ManyToManyField(Employee, related_name='+')
    leader = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='+')
    priority = models.CharField(choices=(('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')), max_length=100)
    files = models.FileField(upload_to='media/task_files', null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(
        choices=(('Pending', 'Pending'), ('In progress', 'In progress'), ('Completed', 'Completed')), max_length=100,
        default='Pending')
    completed_date = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.task


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='+')
    commented_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='+')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    date = models.DateField()
    punch_in = models.DateField(unique_for_date=True)
    punch_out = models.DateField()
    logged_time = models.CharField(max_length=10)
    status = models.CharField(choices=(('Present', 'Present'), ('Absent', 'Absent'), ('On leave', 'On Leave')),
                              default='Absent', max_length=20)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.employee.first_name + self.employee.last_name + ' : ' + str(self.date)


class Timesheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    date = models.DateField()
    activity = models.CharField(max_length=200)
    time_taken = models.CharField(max_length=5)
    remarks = models.CharField(max_length=200, null=True, blank=True)


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    leave_type = models.CharField(
        choices=(('Half day', 'Half day'), ('Short Leave', 'Short Leave'), ('Multiple days', 'Multiple days'),
                 ('One day', 'One day')), max_length=50)
    from_date = models.DateField()
    to_date = models.DateField
    remarks = models.CharField(max_length=200)
    status = models.CharField(choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')),
                              default='Pending', max_length=30)
    leave_balance = models.CharField(max_length=10, default=0)


class Holiday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    location = models.ManyToManyField(Depot)
    remarks = models.CharField(max_length=100)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name + str(self.date)


class Tickets(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    subject = models.CharField(max_length=100)
    remarks = models.CharField(max_length=500)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateField(auto_now=True)
    status = models.CharField(choices=(('Pending', 'Pending'), ('In process', 'In process'), ('Closed', 'Closed')),
                              default='Pending', max_length=50)
    comment = models.CharField(max_length=200, null=True, blank=True)
    update_date = models.DateField()
    closed_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.subject + self.status


class Todo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    date = models.DateField()
    subject = models.CharField(max_length=100)
    todo = models.CharField(max_length=500)
    status = models.CharField(choices=(('Pending', 'Pending'), ('Done', 'Done')), max_length=50, default='Pending')
