from django.http import response
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Account
# Create your views here.


def index(request):
    print('hii')
    return render(request,'index.html')

def signup(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone number')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user_datails = User(username=uname,first_name=name,password=password,email=email)
        user_datails.save()
        if user_datails:
            print(name, email, phone,uname,password)
            return render(request,'signin.html')      
    return render(request,'signup.html')

def signin(request):
    if request.method =="POST":
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user_datails = User.objects.filter(username=uname,password=password)
        if user_datails:
            return redirect('/create_account/')
        else:
            message ={"message":"Please enter valid"}
            return render(request,"signin.html", message)
    return render(request,'signin.html')

def create_account(request):
    if request.method =="POST":
        num = request.POST.get('num')
        name = request.POST.get('name')
        Des = request.POST.get('Des')
        actype = request.POST.get('drop1', None)
        print(actype)
        op_blance = request.POST.get('op_blance')
        cr_balance = request.POST.get('cr_balance')
        print('ggggggggggggg',num,name, Des, actype, op_blance,cr_balance)
        account_save = Account(account_number = num,account_name = name,description  = Des,
            account_type = actype,opening_balance = op_blance,current_balance = cr_balance)
        account_save.save()
        if account_save:
            return redirect('/account_list/')
        return render(request,"create.html")
    return render(request,"create.html")      


def account_list(request):
    data = Account.objects.all()
    return render(request,"table.html", {"data":data})

def edit(request, id):
     data = Account.objects.filter(id=id)
     return render(request,"Edit.html", {"data":data})
def update1(request,id):
    data = Account.objects.filter(id=id)
    num = request.POST.get('num')
    name = request.POST.get('name')
    Des = request.POST.get('Des')
    actype = request.POST.get('drop1', None)
    op_blance = request.POST.get('op_blance')
    cr_balance = request.POST.get('cr_balance')
    data.update(account_number = num,account_name = name,description  = Des,
            account_type = actype,opening_balance = op_blance,current_balance = cr_balance)
    return redirect('/account_list/')
def delete_id(request, id):
    data = Account.objects.filter(id=id).delete()
    return redirect('/account_list/')
