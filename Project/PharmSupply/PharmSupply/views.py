from django.http import HttpResponse 
from django.shortcuts import render , redirect
from PharmSupply.models import Register
from django.contrib import messages
from .form import ImageForm 
from .models import Image 
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def UserRegistration(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('phoneno') and request.POST.get('aadhar') and request.POST.get('password1') and request.POST.get('gender'):
            s=Register()
            s.first_name=request.POST.get('first_name')
            s.last_name=request.POST.get('last_name')
            s.email=request.POST.get('email')
            s.phoneno=request.POST.get('phoneno')
            s.aadhar=request.POST.get('aadhar')
            s.password1=request.POST.get('password1')
            #s.password2=request.POST.get('password2')
            s.gender=request.POST.get('gender')
            if Register.objects.filter(email=s.email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                s.save()
                messages.success(request,'Registered successfully')
                return render(request,'login.html')
            
    else:
        return render(request,'register.html')
def login(request):
    if request.method=="POST":
        try:
            Userdetails=Register.objects.get(email=request.POST['email'],password1=request.POST['password1'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            return redirect('home')
        except Register.DoesNotExist as e:
            messages.success(request,'Email / Password Invalid')
    return render(request,'login.html')


def order(request):
    return render(request,'order.html')
    
def uploadpic(request):
    if request.method == "POST": 
        form=ImageForm(data=request.POST,files=request.FILES) 
        if form.is_valid(): 
            form.save() 
            obj=form.instance 
            return render(request,"uploadpic.html",{"obj":obj}) 
    else: 
        form=ImageForm() 
        img=Image.objects.all() 
    return render(request,"uploadpic.html",{"img":img,"form":form})