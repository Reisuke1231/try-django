from django.contrib.auth import authenticate, login as dj_login
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {'error': 'Invalid username or password.'}
            return render(request, 'accounts/login.html', context)

        dj_login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', {})

def logout(request):
    return render(request, 'accounts/logout.html', {})

def register(request):
    return render(request, 'accounts/register.html', {})