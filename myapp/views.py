from django.shortcuts import render
from .models import Viewers
# Create your views here.

def home(req):
    return render(req,'home.html')
def tvshow(req):
    return render(req,'tvshow.html')
def movies(req):
    return render(req,'movies.html')
def games(req):
    return render(req,'games.html')
def popular(req):
    return render(req,'popular.html')
def mylist(req):
    return render(req,'mylist.html')
def browse(req):
    return render(req,'browse.html')
def register(req):
    if req.method == "POST":
        username=req.POST.get('username')
        email=req.POST.get('email')
        password=req.POST.get('password')
        confirmpass=req.POST.get('confirmpass')
        subscription=req.POST.get('subscription')
        user=Viewers.objects.filter(email=email)
        print(username)
        print(email)
        print(password)
        print(subscription)
        if user:
            eml="Email is already exist"
            return render(req,'register.html',{'email':eml})
        else:
            if confirmpass==password:
                 Viewers.objects.create(username=username,email=email,password=password,subscription=subscription)
                 msg="Data successfully saved"
                 return render(req,'login.html',{'msg':msg})

            else:
                pwd="password not matched"
                return render(req,'register.html',{'pwd':pwd})
            
    return render(req,'register.html')
def login(req):
    return render(req,'login.html')
def logindata(req):
    if req.method=="POST":
        email=req.POST.get('email')
        password=req.POST.get('password') 
        user=Viewers.objects.filter(email=email)
        if user:
            userdata=Viewers.objects.get(email=email)
            pass1=userdata.password
            if password==pass1:
                data={'id':userdata.id,'name':userdata.username,'email':userdata.email,'password':userdata.password,'subscription':userdata.subscription}
                return render(req,'dashboard.html',{'data':data})
            else:
                msg="Password not matched"
                return render(req,'login.html',{'alert':msg})  
        else:
            msg="Email not register"
            return render(req,'register.html',{'alert':msg})  
def dashboard(req):
     return render(req,'dashboard.html')
def logout(req):
     return render(req,'logout.html')
