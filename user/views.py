from django.shortcuts import render,redirect                                                                                                                                                                   
from user.models import About                                                                                                                                                                   
from django.contrib.auth import authenticate                                                                                                                                                                   

def about(request):
    abouts = About.objects.all()                                                                                                                                                                   

    context = {                                                                                                                                                                   
        'abouts' : abouts,                                                                                                                                                                   
    }                                                                                                                                                                   

    return render(request, "about.html", context=context)                                                                                                                                                                   

def user_login(request):                                                                                                                                                                   
    if request.method == 'POST':                                                                                                                                                                   

        username = request.POST.get("username")                                                                                                                                                                   
        password = request.POST.get("password")                                                                                                                                                                   

        user = authenticate(username=username,password=password)                                                                                                                                                                   

        if user is not None:
            request.session['username'] = username
            return redirect("/")

    return render(request, "login.html")