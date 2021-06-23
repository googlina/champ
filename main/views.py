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
