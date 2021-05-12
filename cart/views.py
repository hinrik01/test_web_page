from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cereal.models import Cereal, CerealImage
from cart.models import Cart, CartCereal
from order.models import OrderItems
from django.http import JsonResponse
import json


# Create your views here.

@login_required
def add_to_cart(request, cereal_id, quantity):
    user_cart = Cart.objects.filter(user=request.user).first()
    cereal = Cereal.objects.filter(id=cereal_id).first()
    previous_item = CartCereal.objects.filter(cereal=cereal, cart=user_cart).first()
    if previous_item is not None:
        previous_item.quantity += quantity
        previous_item.save()
    else:
        cart_cereal_instance = CartCereal(
            cereal=cereal,
            cart=user_cart,
            quantity=quantity
        )
        cart_cereal_instance.save()
    return redirect('cereal-details', id=cereal_id)


@login_required
def cart(request):
    if request.method == 'POST':
        return redirect('update-quantity-cart',
                        cereal_id=request.POST.get('cereal_id'),
                        quantity=request.POST.get('quantity', default=1))

    cart_json = get_cart(request)
    context = json.loads(cart_json.content)

    return render(request, 'cart/cart.html', context)


@login_required
def get_cart(request):
    user_cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartCereal.objects.filter(cart=user_cart)
    cart_total_price = total_price(request)

    cart_items_obj = [{
        'cereal_id': cart_item.cereal.id,
        'cereal_name': cart_item.cereal.name,
        'cereal_price': cart_item.cereal.price,
        'quantity': cart_item.quantity,
        'cereal_image': CerealImage.objects.filter(cereal_id=cart_item.cereal.id).first().image
    } for cart_item in cart_items]

    cart_obj = {
        'cart_items': cart_items_obj,
        'total_price': cart_total_price
    }

    return JsonResponse({'data': cart_obj})


@login_required
def delete_from_cart(request, cereal_id):
    user_cart = Cart.objects.filter(user=request.user).first()
    cereal = Cereal.objects.filter(id=cereal_id).first()
    cart_item = CartCereal.objects.filter(cereal=cereal, cart=user_cart).first()
    cart_item.delete()
    return redirect('cart')


@login_required
def update_quantity(request, cereal_id, quantity):
    user_cart = Cart.objects.filter(user=request.user).first()
    cereal = Cereal.objects.filter(id=cereal_id).first()
    cart_item = CartCereal.objects.filter(cereal=cereal, cart=user_cart).first()
    cart_item.quantity = quantity
    cart_item.save()
    return redirect('cart')


@login_required
def clear(request):
    clear_cart(request)
    return redirect('cart')


@login_required
def clear_cart(request):
    user_cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartCereal.objects.filter(cart=user_cart)
    cart_items.delete()


@login_required
def add_to_cart_buy_now(request, cereal_id, quantity):
    user_cart = Cart.objects.filter(user=request.user).first()
    cereal = Cereal.objects.filter(id=cereal_id).first()
    previous_item = CartCereal.objects.filter(cereal=cereal, cart=user_cart).first()
    if previous_item is not None:
        previous_item.quantity += quantity
        previous_item.save()
    else:
        cart_cereal_instance = CartCereal(
            cereal=cereal,
            cart=user_cart,
            quantity=quantity
        )
        cart_cereal_instance.save()
    return redirect('payment-step')


@login_required
def buy_single_item(request, cereal_id, quantity):
    clear_cart(request)
    return add_to_cart_buy_now(request, cereal_id, quantity)


@login_required
def rebuy_order(request, order_id):
    clear_cart(request)
    user_cart = Cart.objects.filter(user=request.user).first()
    order_cart_items = OrderItems.objects.filter(order_id=order_id)
    for user_item in order_cart_items:
        cart_cereal = CartCereal(
            cereal=user_item.cereal,
            cart=user_cart,
            quantity=user_item.quantity
        )
        cart_cereal.save()
    return redirect('payment-step')


@login_required
def total_price(request):
    user_cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartCereal.objects.filter(cart=user_cart)
    total = 0
    for item in cart_items:
        total += item.cereal.price * item.quantity
    return total


@login_required
def check_cart(request):
    user_cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartCereal.objects.filter(cart=user_cart)
    if not cart_items:
        return redirect('cart')
    else:
        return redirect('payment-step')
