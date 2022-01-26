from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderFrom
from .filters import OrderFilter

# Create your views here.
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

def products(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request , 'products.html',context)

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

def delete_order(request,pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        #print("Print Post",request.POST)
        order.delete()
        return redirect('/')

    context = {"order":order}
    return render(request,'delete_order.html',context)










