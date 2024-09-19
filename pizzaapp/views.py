from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def admin_login_view(request):
    return render(request,'pizzaapp/admin-login.html')

def authenticate_admin_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request,user)
        return redirect('admin-home')
    else :
        messages.add_message(request, messages.ERROR,'invalid credentials.')
        return redirect('admin-login')

def admin_logout_view(request):
    logout(request)
    return redirect('admin-login')

def admin_home_view(request):
    return render(request, 'pizzaapp/admin-home.html')

