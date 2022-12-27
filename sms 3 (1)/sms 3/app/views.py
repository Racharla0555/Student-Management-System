from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def index(r):
    return render(r,'index.html')
def studentsignin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('/home')
        else:
            messages.error(request,"Invalid login credentials")
    return render(request,'slogin.html')
def studentsignup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=password
        if password!=password1 :
            messages.error(request,"Passwords not matches")
        elif User.objects.filter(username=username):
            messages.error(request,"Username already exists...!")
        elif User.objects.filter(email=email):
            messages.error(request,"Email already taken...!")
        elif len(password)<8:
            messages.error(request,"Password must be eight characters")
        else:
            User.objects.create_user(username=username,email=email,password=password)
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/home')
    return render(request,'ssignup.html')
def facultysignin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('/home')
        else:
            messages.error(request,"Invalid login credentials")
    return render(request,'flogin.html')
def facultysignup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=password
        if password!=password1 :
            messages.error(request,"Passwords not matches")
        elif User.objects.filter(username=username):
            messages.error(request,"Username already exists...!")
        elif User.objects.filter(email=email):
            messages.error(request,"Email already taken...!")
        elif len(password)<8:
            messages.error(request,"Password must be eight characters")
        else:
            User.objects.create_user(username=username,email=email,password=password)
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    return render(request,'fsignup.html')
@login_required()
def home(r):
    return render(r,'home.html')
def branch(r):
    return render(r,'cse.html')
from app.models import *
def addstudent(r):
    if r.method=="POST":
        name=r.POST['name']
        hall=r.POST['hall']
        section=r.POST['section']
        batch=r.POST['batch']
        year=r.POST['year']
        sem=r.POST['sem']
        Student(name=name,hall=hall,section=section,batch=batch,year=year,sem=sem).save()
        return redirect('/viewstudent')
    return render(r,'newrecord.html')
def sign(r):
    logout(r)
    return redirect('/')
def addit(r):
    if r.method=="POST":
        name=r.POST['name']
        hall=r.POST['hall']
        section=r.POST['section']
        batch=r.POST['batch']
        year=r.POST['year']
        sem=r.POST['sem']
        attendance=r.POST['attendance']
        Student(name=name,hall=hall,section=section,batch=batch,year=year,sem=sem,attendance=attendance).save()
        return redirect('/viewstudent')
    return render(r,'addit.html')
def viewit(r):
    student=Student.objects.order_by('hall')
    return render(r,'viewit.html',{'stud':student})
from .forms import *
def add(request):
    form=Studentform()
    if request.method=="POST":
        form=Studentform(data=request.POST,files=request.FILES)
        hall=request.POST['hall_ticket']
        a=iStudent.objects.filter(hall_ticket=hall.upper())
        if a:
            messages.error(request,"Student already exists")
        elif form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request,"add.html",{'form':form})  
def cse(r):
    return render(r,'cse 2.html')
def it(r):
    return render(r,'inf.html')
def ece(r):
    return render(r,'ece.html')
def mec(r):
    return render(r,'mech.html')
def civ(r):
    return render(r,'civil.html')
def viewstudent(r):
    student=Student.objects.order_by('hall')
    return render(r,'view.html',{'stud':student})
def view(r,id):
    stud=Student.objects.get(id=id)
    return render(r,'student.html',{'i':stud})
def remov(r,id):
    stud=Student.objects.get(id=id)
    stud.delete()
    return redirect('/viewstudent')