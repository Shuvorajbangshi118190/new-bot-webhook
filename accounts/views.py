from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser
from dashboard.views import dashboard

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if email and password:
            user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            
            login(request, user)
            return redirect('home')
        else:
            error_message = "Please provide valid email and password."
            return render(request, 'registration.html', {'error_message': error_message})
    return render(request, 'registration.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                
                return redirect(dashboard)
            else:
               
                error_message = "Invalid login credentials."
                return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = "Please provide email and password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

