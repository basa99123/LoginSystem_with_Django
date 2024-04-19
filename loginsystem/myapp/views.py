from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        passw1 = request.POST['password1']
        pass2 = request.POST['password2']
        if passw1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username= user).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username= user, email=email, password= passw1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password is not same")
            return redirect('register')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        passw = request.POST['password1']
        user = auth.authenticate(username = user, password = passw)

        if user is not None:
            auth.login(request,user)
            return render(request, 'user_login.html')
        else:
            messages.info('credentials Invalid')
            return redirect('login')
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')