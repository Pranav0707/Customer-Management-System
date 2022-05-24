from django.db.models import fields, query
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from cms_app.decorators import allowed_user, unauthenticated,admin_only
from cms_app.forms import  CreateCustomerForm, CustomerForm, OrderForm, ProductForm,RegistrationForm, UserOrderForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import *


# Create your views here.

@unauthenticated
def userRegistration(request):
  
        form=RegistrationForm()

        if request.method=='POST':
            form=RegistrationForm(request.POST)
        if form.is_valid():
            
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user = user
            )
            messages.success(request,'Account created for : ' + username)
            return redirect('login')

        context={'form':form}
        return render(request,'cms_app/registeration.html',context)
            
@unauthenticated
def UserLogin(request):
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username Or Password Is Incorrect!!')
                

        context={}
        return render(request,'cms_app/login.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def accountsettings(request):
    customer=request.user.customer
    form=CustomerForm(instance=customer)

    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid:
            form.save()
    context={'form':form}
    return render(request,'cms_app/account_settings.html',context)

def UserLogout(request):
    logout(request)
    return redirect('login')





@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def UserPage(request):
    orders=request.user.customer.order_set.all()
    total_orders=orders.count()
    orders_delivered=orders.filter(status='Delivered').count()
    orders_pending=orders.filter(status='Pending').count()
    context={'orders':orders,'total_orders':total_orders,'orders_delivered':orders_delivered,'orders_pending':orders_pending}
    return render(request,'cms_app/user.html',context)


@login_required(login_url='login')
@admin_only
def Home(request):
    order=Order.objects.all()
    customer=Customer.objects.all()

    total_orders=order.count()
    total_customers=customer.count()

    orders_delivered=order.filter(status='Delivered').count()
    orders_pending=order.filter(status='Pending').count()

    context={'order':order,'customer':customer,'total_orders':total_orders,'total_customers':total_customers,
            'orders_delivered':orders_delivered,'orders_pending':orders_pending}

    return render(request,'cms_app/dashboard.html',context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def product(request):
    product=Product.objects.all()
    product_form=ProductForm()
    if request.method=="POST":
        product_form=ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
    context={'product':product,"product_form":product_form}
    return render(request,'cms_app/product.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    order=customer.order_set.all()
    order_count=order.count()
    filter=OrderFilter(request.GET,queryset=order)
    order=filter.qs
    context={'customer':customer,'order':order,'order_count':order_count,'filter':filter}
    return render(request,'cms_app/customer.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def orderform(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=3)
    customer=Customer.objects.get(id=pk)
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    #form=OrderForm(initial={'customer':customer})


    if request.method=='POST':
       #form=OrderForm(request.POST)
       formset=OrderFormSet(request.POST,instance=customer)
       if formset.is_valid():
           formset.save()
           return redirect('/')
    context={'formset':formset}
    return render(request,'cms_app/orderform.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateorder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
       form=OrderForm(request.POST,instance=order)
       if form.is_valid:
           form.save()
           return redirect('/')
    context={'form':form}
    return render(request,'cms_app/updateorder.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteorder(request,pk):
    deleteorder=Order.objects.get(id=pk)
    if request.method=='POST':
        deleteorder.delete()
        return redirect('/')
    context={'deleteorder':deleteorder}
    return render(request,'cms_app/deleteorder.html',context)

@login_required
def create_user_order(request,id):
    try:
        customer=get_object_or_404(Customer,id=id)
        print(customer)
    except Exception as e:
        customer=None
        print(e)
    form=UserOrderForm()
    customer=request.user.customer
    if request.method=="POST":
        form=UserOrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.customer=customer
            instance.save()

    context={"form":form}
    return render(request,'cms_app/create_user_order.html',context)

def create_customer(request):
    form=CreateCustomerForm()
    
    if request.method=="POST":
        form=CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context={"form":form}
    return render(request,'cms_app/create_customer.html',context)