from django.forms import ModelForm

from backend.models import Department, Designation, Employee, Project


class Add_Employee_Form(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ('id',)


class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class AddDepartmentForm(ModelForm):
    class Meta:
        model= Department
        fields = ('department','description')


class AddDesignationForm(ModelForm):
    class Meta:
        model= Designation
        fields = ('department','designation')