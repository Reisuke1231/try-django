from django.contrib.auth import login as dj_login, logout as dj_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            dj_login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)

    context = {"form": form}

    return render(request, 'accounts/login.html', context=context)


def logout(request):
    if request.method == 'POST':
        dj_logout(request)
        return redirect('/login/')
    return render(request, 'accounts/logout.html', {})
