from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def user_log(request):
    if request.method == 'POST':
        userName = request.POST['usernm']
        userPassword = request.POST['userpasswd']
        user = authenticate(request, usern=userName, userp=userPassword)

        if user is not None:
            login(request,user)
            return redirect('Home')

            #print('UserEmail:' +userEmail)
        else:
            print('User not Found.')

    return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return redirect('Login')