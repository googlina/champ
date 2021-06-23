from django.forms import ModelForm

from backend.models import Employee, Project


class Add_Employee_Form(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
