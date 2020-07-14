from django.shortcuts import HttpResponse,render,redirect
from home.models import Contact
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')
def downloads(request):
    return render(request,'downloads.html')
def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        query = request.POST.get("query")
        print(name,email,phone,query)
        contact = Contact(name=name,email=email,phone=phone,query=query)
        contact.save()
    return render(request,'contact.html')

def loginuser(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        if User.objects.filter(username=email).exists()==False:
            user1= User.objects.create_user(username=email,password=password)
            user1.save()
            user=auth.authenticate(username=email,password=password)
            user.save()
            login(request,user)
            print("Logged in successfully-->"+str(request.user))
            return redirect('/')
        
    return  render(request,'login.html')

def logoutuser(request):
     logout(request)
     print("Logged out successfully-->"+str(request.user))
     return HttpResponse("<h1 style='color:green'>You are logged out now</h1>")

def signin(request):
    return render(request,'signin.html')