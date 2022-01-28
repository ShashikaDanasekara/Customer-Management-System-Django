from django.shortcuts import render,redirect
from django.forms import inlineformset_factory

from accounts.decorators import unauthenticated_user,allowed_users,admin_only

from .models import *
from .forms import OrderFrom,CreateUserForm
from .filters import OrderFilter

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group

# Create your views here.

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            return redirect('login')

    context = {"form":form}
    return render(request, 'register.html',context)

@unauthenticated_user
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request,"user name or password is incorrect!")

    context = {}
    return render(request, 'login.html',context)

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        "orders":orders,
        "customers":customers,
        "total_customers":total_customers,
        "total_orders":total_orders,
        "delivered":delivered,
        "pending":pending
    }

    return render(request , 'dashboard.html',context)

def user_page(request):
    context = {}
    return render(request , 'user.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','superadmin'])
def products(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request , 'products.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','superadmin'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders=orders.count()

    my_filter = OrderFilter(request.GET,queryset=orders)
    orders = my_filter.qs

    context = {
        "customer":customer,
        "orders":orders,
        "total_orders":total_orders,
        "my_filter":my_filter,
    }

    return render(request , 'customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','superadmin'])
def create_order(request):
    form = OrderFrom()

    if request.method == 'POST':
        #print("Print Post",request.POST)
        form = OrderFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form":form}

    return render(request,'order_form.html',context)

@login_required(login_url='login')
def create_single_order(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'),extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)

    if request.method == 'POST':
        #print("Print Post",request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {"formset":formset}

    return render(request,'order_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','superadmin'])
def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderFrom(instance=order)

    if request.method == 'POST':
        #print("Print Post",request.POST)
        form = OrderFrom(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form":form}
    return render(request,'order_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','superadmin'])
def delete_order(request,pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        #print("Print Post",request.POST)
        order.delete()
        return redirect('/')

    context = {"order":order}
    return render(request,'delete_order.html',context)










