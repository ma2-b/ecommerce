from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

import json

from .models import Order, OrderItem, Product, Category

# Create your views here.
def home(request):
    data = Product.objects.all()
    products = []
    counter = 0
    for i in data:
        if counter >= 6:
            break
        products.append(i)
        counter+=1
    
    if request.user.is_authenticated:
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.cart_items
        
    else:
        items = []
        order = {'cart_total':0, 'cart_items':0}
        cartItems = order['cart_items']     
        
    context = {"products":products, 'cartItems':cartItems}
    return render(request,"market/index.html",context)


class ShopListView(ListView):
    model = Product
    template_name = "market/shop.html"
    context_object_name = "products"
    paginate_by = 6
    
    
def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.cart_items
    else:
        items = []
        order = {'cart_total':0, 'cart_items':0}
        cartItems = order['cart_items']
        
    context = {'items': items, 'order':order, 'cartItems':cartItems}
    return render(request, 'market/cart.html', context)
   
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.cart_items
    else:
        items = []
        order = {'cart_total':0, 'cart_items':0}
        cartItems = order['cart_items']
        
    context = {'items': items, 'order':order, 'cartItems':cartItems}
    return render(request, 'market/checkout.html', context)
    
    
def updateItem(request):
    data = json.loads(request.body)
    
    productId = data['productId']
    action = data['action']
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse("Item was added", safe=False)

def process_order(request):
    print('data:', request.body)

    return JsonResponse("payment complete", safe=False)



    

