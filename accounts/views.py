from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()

        return redirect('/login')
    context = {"form": form}
    return render(request, "accounts/register.html", context=context)


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
    if request.method == 'POST':
        dj_logout(request)
        return redirect('/login/')
    return render(request, 'accounts/logout.html', {})
