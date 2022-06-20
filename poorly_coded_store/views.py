from django.shortcuts import render , redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if request.method != 'POST':
        return  redirect('/')
    
    quantity_from_form = int(request.POST["quantity"])
    id = request.POST["id"]
    price = float(Product.objects.get(id=id).price)
    total_charge = quantity_from_form * price
    print("Charging credit card...")
    
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    
    
    return redirect('/checkout/Final')

def checkoutFinal(request):
    allOrders = Order.objects.all()
    total = 0
    totalQuantity = 0
    for order in allOrders:
        total += order.total_price 
        totalQuantity += order.quantity_ordered


    context ={
        'total': total,
        'totalQuantity':totalQuantity,
        'order': order,
        'orders_count': len(allOrders)
    }
    return render(request, "store/checkout.html",context)