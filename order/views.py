from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from order.forms.address_form import AddressForm
from order.forms.payment_form import PaymentForm
from order.models import Order, Address, Country, OrderItems
from user.models import Profile
from cart.models import Cart, CartCereal
from cart.views import clear_cart

# Create your views here.
from cereal.models import Cereal


@login_required
def payment(request):
    profile = Profile.objects.filter(user=request.user).first()
    address = Address.objects.filter(id=profile.address_id).first()

    if address is None:
        address = Address()
        address.save()

        has_address = False
    else:
        has_address = True

    clear_incomplete_order(request.user)

    new_order = Order(
        order_completed=False,
        address=address,
        user=request.user
    )
    new_order.save()

    copy_cart_to_order(new_order)

    order_items = OrderItems.objects.filter(order=new_order)

    total_price_payment = total_price(order_items)

    if request.method == 'POST':
        address_form = AddressForm(instance=address, data=request.POST)
        payment_form = PaymentForm(data=request.POST)
        if address_form.is_valid() and payment_form.is_valid():
            address = address_form.save()
            new_order.save()

            # Checks if save address to profile was selected and adds the address to user profile
            if request.POST.get('save_address', default=None) == 'on':
                profile.address = address
                profile.save()
            return redirect('review-step')
        else:
            return render(request, 'order/payment.html', {
                'order_items': order_items,
                'address_form': address_form,
                'payment_form': payment_form,
                'total_price': total_price_payment,
                'has_address': has_address
            })

    else:
        address_form = AddressForm(instance=address)  # Attempts to fetch the user profile's address
        payment_form = PaymentForm()
        return render(request, 'order/payment.html', {
            'order_items': order_items,
            'address_form': address_form,
            'payment_form': payment_form,
            'total_price': total_price_payment,
            'has_address': has_address
        })


def copy_cart_to_order(order):
    user_cart = Cart.objects.filter(user=order.user).first()
    user_cart_items = CartCereal.objects.filter(cart=user_cart)
    for user_item in user_cart_items:
        order_item = OrderItems(
            cereal=user_item.cereal,
            order=order,
            quantity=user_item.quantity
        )
        order_item.save()


def clear_incomplete_order(user):
    # Checks if an old order exists in the system, that is not completed. If so it deletes it.
    old_order = Order.objects.filter(user=user, order_completed=False)
    if old_order.exists():
        old_order = old_order.first()
        old_address = Address.objects.filter(id=old_order.address_id).first()
        profile = Profile.objects.filter(user=user).first()
        if profile.address is None:
            old_address.delete()
        old_order.delete()


# Fetches all order data and displays it for confirmation
@login_required
def review(request):
    order = Order.objects.filter(user=request.user, order_completed=False).first()
    items = OrderItems.objects.filter(order=order)
    total_price_review = total_price(items)
    address = order.address

    return render(request, 'order/review.html', {
        'items': items,
        'total_price': total_price_review,
        'address': address,
    })


# Last step in payment, when order has been placed
@login_required
def confirmation(request):
    clear_cart(request)
    try:
        order = get_object_or_404(Order, user=request.user, order_completed=False)
        items = OrderItems.objects.filter(order=order)
        order.order_completed = True  # Changes order status to complete
        order.save()
        return render(request, 'order/confirmation.html', {
            'order': order,
            'items': items
        })
    except:
        return redirect('cereal-index')


def total_price(items):
    price = 0
    for item in items:
        price += item.cereal.price * item.quantity
    return price
