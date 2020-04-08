from django.shortcuts import render, get_object_or_404, redirect
from store.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def product_details(request):
    context = {

        'products' : Product.objects.all()
    }
    return render(request, 'products/index.html', context)


def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)


    return render(request, 'products/index3.html', {'product':product[0]})

@login_required
def add_to_cart(request, itemid):
     product=get_object_or_404(Product,id= itemid)
     
     loged_user=get_object_or_404(Customer, user=request.user)
     #cart= Cart.objects.filter(cart_identifier=loged_user)
     cart=get_object_or_404(Cart,cart_identifier=loged_user)
     if CartElement.objects.filter(cart=cart,product=product).exists():
         cart_item=CartElement.objects.get(cart=cart,product=product)
         cart_item.quantity+=1
         cart_item.save()
     else:
         CartElement.objects.create(cart=cart,product=product)
     
     return redirect('product-list')


def remove_from_cart(request, cart_element_id):
    if get_object_or_404(CartElement, id=cart_element_id).quantity==1:
        CartElement.objects.filter(id=cart_element_id).delete()
    else:
        cart_item=CartElement.objects.get(id=cart_element_id)
        cart_item.quantity=cart_item.quantity-1
        cart_item.save()
    
    return redirect('cart_details')


    

def cart_details(request):
    loged_user=get_object_or_404(Customer, user=request.user)
    #cart= Cart.objects.filter(cart_identifier=loged_user)
    cart=get_object_or_404(Cart,cart_identifier=loged_user)
    context ={

        'elements': CartElement.objects.filter(cart=cart)
    }

    return render(request, 'products/cartpage.html', context )