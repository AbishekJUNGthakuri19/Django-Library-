from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# # Create your views here.


def signup(request):
    erorr_message = None

    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 != pass2:
            erorr_message = "Your password and confirm password is not same"
        else:
            if User.objects.filter(username = uname).exists():
                erorr_message = "Name is taken"
            if User.objects.filter(email = email).exists():
                erorr_message = "Email is taken"
            else:
                myuser = User.objects.create_user(uname,email,pass1)
                myuser.save()
                return redirect('login')
        
    return render(request, 'signup.html', {'error_message': erorr_message})

def loginPage(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass']

        user = authenticate(request, username = username, password = pass1)

        if user is not None:
            login(request,user)
            return redirect('library')
        
        else:
            error_message = 'Your username or password is incorrect'
    
    return render(request,'login.html',{'error_message':error_message})



