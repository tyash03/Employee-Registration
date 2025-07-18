from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'signup.html', {'form': form})

    

def loginpage(request):
    if request.method== 'POST':
        usr = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request,username=usr,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username and password not correct. Please try again')
    return render(request,'login.html')



def home(request):
    return render(request, 'home.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('login')
            
@login_required
def addemployee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewemployee')
    else:
        form = AddEmployeeForm()
    return render(request,'addemployee.html',{'form':form})

@login_required
def viewemployee(request):
    employees = Employee.objects.all()
    return render(request, 'viewemployee.html', {'employee':employees})


def deleteemoployee(request, empid):
    data = Employee.objects.get(empid=empid)
    data.delete()
    employees= Employee.object.all()
    return render(request,'viewemployee',{'employees': employees})


def editemployee(request,empid):
    data= Employee.objects.get(empid=empid)
    return render(request,'editemployee.html',{'data':data})

def updateemployee(request,empid):
    data = Employee.objects.get(empid=empid)
    form=AddEmployeeForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        form.save()
        return redirect('viewemployee')
    else:
        return render(request, 'editemployee.html',{'data' :data })


