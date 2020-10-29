from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        exist = bool(User.objects.filter(username=username))
        if password1 == password2:
            if not exist:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                return redirect("login")
            else:
                messages.info(request, "UserName Already Exist")
                return redirect("register")
        else:
            messages.info(request, "PassWord is not Matching you idiot ")
            return redirect("register")
    else:
        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        #password checking stuff
        username = request.POST['username']
        password = request.POST['password']
        #print(username ,"  ", password)
        
        user_obj = auth.authenticate(request=request ,username=username, password=password)
        
        if user_obj is not None:
            auth.login(request, user_obj)
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")
    else:
        return render(request, "login.html")