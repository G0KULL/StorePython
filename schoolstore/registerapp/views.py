from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request, "login.html")


def new(request):
    return render(request, "base.html")


def form(request):
    return render(request, "form.html")


def confirmation(request):
    return render(request, "submit.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')

        else:

            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('')
    return render(request, "register.html")
