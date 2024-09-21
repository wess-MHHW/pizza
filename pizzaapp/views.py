from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from pizzaapp.models import Customer, Item, Order, Pizza
from django.db.models import OuterRef, Subquery


# Create your views here.

# admin views
def admin_login_view(request):
    return render(request,'pizzaapp/admin-login.html')

def authenticate_admin_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None and user.is_superuser:
        login(request,user)
        return redirect('admin-home')
    else :
        messages.add_message(request, messages.ERROR,'invalid credentials.')
        return redirect('admin-login')

@login_required
def admin_home_view(request):
    context = {"pizzas":Pizza.objects.all()}
    return render(request, 'pizzaapp/admin-home.html',context)

@login_required
def admin_logout_view(request):
    logout(request)
    return redirect('admin-login')

@login_required
def add_pizza_view(request):
    name = request.POST['name']
    price = request.POST['price']

    Pizza(name=name, price=price).save()
    return redirect('admin-home')

@login_required
def delete_pizza_view(request, id):
    Pizza.objects.get(id=id).delete()
    return redirect('admin-home')

@login_required
def admin_orders_view(request):
    
    order_list = []
    orders = Order.objects.all()
    
    for order in orders:
        items = Item.objects.filter(order=order)
        order_list.append({
                "id": order.id,
                "user": order.user,
                "address": order.address,
                "status": order.status,
                "created_at": order.created_at,
                "items": items,
                "total":round(sum(float(item.pizza.price) * float(item.quantity) for item in items),2)
        })

    
    context={"orders":order_list}
    return render(request, "pizzaapp/admin-orders.html",context)

@login_required
def admin_accept_order_view(request, id):
    order = Order.objects.get(id=id)
    order.status = "Accepted" 
    order.save()
    return redirect(request.META['HTTP_REFERER'])

@login_required
def admin_decline_order_view(request,id):
    order = Order.objects.get(id=id)
    order.status = "Declined" 
    order.save()
    return redirect(request.META['HTTP_REFERER'])
# customer views
def customer_register_view(request):
    return render(request,'pizzaapp/customer-register.html')

def customer_create_view(request):
    username = request.POST['username']
    phone = request.POST['phone number']
    password = request.POST['password']

    if User.objects.filter(username=username):
        messages.add_message(request, messages.ERROR, 'Username already in use.')
        return redirect('customer-register')

    user  = User.objects.create_user(username=username, password=password)
    Customer.objects.create(user=user, phone=phone)
    login(request,user)
    messages.add_message(request, messages.SUCCESS, 'User successfully created.')
    return redirect('customer-home')

def customer_login_view(request):
    return render(request,'pizzaapp/customer-login.html')

def authenticate_customer_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request,user)
        return redirect('customer-home')
    else :
        messages.add_message(request, messages.ERROR,'invalid credentials.')
        return redirect('customer-login')

@login_required
def customer_logout_view(request):
    logout(request)
    return redirect('customer-login')

@login_required
def customer_home_view(request):
    context={"pizzas":Pizza.objects.all(), "user":request.user}
    return render(request, "pizzaapp/customer-home.html",context)

@login_required
def customer_order_view(request):
    address = request.POST['address']
    order = Order.objects.create(user=Customer.objects.get(user=request.user), address=address,status='Pending')
    items = []
    for pizza in Pizza.objects.all():
        quantity = int(request.POST.get(str(pizza.id), 0))
        if quantity > 0  :
            items.append(Item(pizza=pizza, quantity=quantity, order=order))
    Item.objects.bulk_create(items)   
    
    messages.add_message(request, messages.SUCCESS, "Order placed successfully.")
    return redirect('customer-home')

@login_required
def customer_orders_view(request):
    
    order_list = []
    orders = Order.objects.filter(user__user_id=request.user.id)
    
    for order in orders:
        items = Item.objects.filter(order=order)
        order_list.append({
                "user": order.user,
                "address": order.address,
                "status": order.status,
                "created_at": order.created_at,
                "items": items,
                "total":round(sum(float(item.pizza.price) * float(item.quantity) for item in items),2)
        })

    
    context={"orders":order_list, "user":request.user}
    return render(request, "pizzaapp/customer-orders.html",context)







