from django.contrib import admin
from .models import CustomUser, Zone, State, Depot, City
from backend.models import Employee, Department, Designation, User_type, Project, PersonalInfo, BankInfo, FamilyInfo, \
    EduInfo, EmergencyContact, WorkExpInfo,Task

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Zone)
admin.site.register(State)
admin.site.register(Depot)
admin.site.register(City)
admin.site.register(User_type)
admin.site.register(FamilyInfo)
admin.site.register(PersonalInfo)
admin.site.register(BankInfo)
admin.site.register(EmergencyContact)
admin.site.register(EduInfo)
admin.site.register(WorkExpInfo)
admin.site.register(Project)
admin.site.register(Task)
