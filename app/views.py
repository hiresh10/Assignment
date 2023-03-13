from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def Index(request):
    return render(request,"app/index.html")
def SignUppage(request):
    return render(request,'app/signup.html')

def Register(request):
    if request.method == 'POST':

        profile = request.POST['profile']

        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']


        user = User.objects.filter(username=username)

        if user:
            message = "User already exists"
            return render(request,"app/signup.html",{'msg':message})

        else:
            if password == cpassword:
                newuser = User.objects.create(profile=profile,username=username,password=password)
                message = "Register successfull"

                return render(request,"app/login.html",{'username':username,'msg':message})
            else:
                message = "Password missmatch!!"
                return render(request,"app/signup.html",{'msg':message})

def LoginPage(request):
    return render(request,"app/login.html")

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = User.objects.get(username=username)

        if user:
            if user.password==password:
                request.session['id'] = user.id
                request.session['username'] = user.username
                request.session['password'] = user.password

                return redirect('home')
            else:
                message = "Password Missmatch"
                return render(request,"app/login.html",{'msg':message})

        else:
            message = "User does not exists"
            return render(request,"app/login.html",{'msg':message})
        
def Home(request):
    return render(request,"app/home.html")