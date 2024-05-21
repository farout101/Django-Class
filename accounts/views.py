from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"username: {username}, password : {password}")
    
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            context = {"error" : "Invalid credentials"}
            return render(request, "accounts/login.html",context)
        
        login(request, user)
        
        return redirect('/admin/')
        
    context = {}
    
    return render(request, "accounts/login.html",context)

def logout_view(request):

    context = {}

    return render(request, "accounts/logout.html",context=context)

def register_view(request):
    context = {}

    return render(request, "accounts/register.html",context=context)