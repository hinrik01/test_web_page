from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from user.forms.profile_form import ProfileForm, UserCreateForm
from order.forms.address_form import AddressForm
from user.models import Profile, Search
from order.models import Address, Country, Order, OrderItems
from cart.models import Cart
from django.contrib.auth.models import User




def register(request):
    """This function saves a new User to the database"""
    # A POST request will save a new user to the database
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()

            # Creates empty user profile in database
            profile = Profile(user=new_user)
            profile.email = new_user.email
            profile.save()

            # Creates empty cart in database
            cart = Cart(user=new_user)
            cart.save()

            return redirect('login')
    # If the request is not a POST a page is rendered to create a new User
    else:
        form = UserCreateForm()

    return render(request, 'user/register.html', {
        'form': form
    })


def view_profile(request):
    """This function displays the profile."""
    profile_instance = Profile.objects.filter(user=request.user)
    # Profile exists
    if not profile_instance.exists():
        # Profile doesn't exist
        profile = Profile(user=request.user)
        profile.save()

    profile = profile_instance.first()

    # Address dose not exist
    if profile.address_id is not None:
        address = Address.objects.filter(id=profile.address_id).first()
    # Address exists
    else:
        address = Address()

    return render(request, 'user/profile.html', {
        'profile': profile,
        'address': address
    })


def edit_profile(request):
    """This function sends the form to edit the profile and saves in when returned"""
    profile = Profile.objects.filter(user=request.user).first()
    # A POST request will update the profile of the user
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    # If not a POST request a page will be rendered to update the profile
    return render(request, 'user/edit_profile.html', {
        'form': ProfileForm(instance=profile)
    })


def edit_address(request):
    """This function sends the form to edit the address and saves in when returned"""
    profile = Profile.objects.filter(user=request.user).first()
    address = Address.objects.filter(id=profile.address_id).first()
    # A POST request will update the address of the user
    if request.method == 'POST':
        form = AddressForm(instance=address, data=request.POST)
        if form.is_valid():
            address = form.save()
            profile.address = address
            profile.save()
            return redirect('profile')
    # If not a POST request a page will be rendered to update the address
    return render(request, 'user/edit_address.html', {
        'form': AddressForm(instance=address)
    })


def delete_address(request):
    """This function deletes the address from a profile"""
    profile = Profile.objects.filter(user=request.user).first()
    profile.address = None
    profile.save()
    return redirect('profile')


def total_price(items):
    total_price = 0
    for item in items:
        total_price += item.cereal.price * item.quantity
    return total_price


def order_history(request):
    """This function displays the order_history of a user"""
    cereal = []
    orders = []
    for x in Order.objects.filter(user=request.user, order_completed=True).order_by("-id"):
        for j in OrderItems.objects.filter(order_id=x.id):
            cereal += [{'cereal': j.cereal, 'quantity': j.quantity}]
        orders += [{
            'id': x.id,
            'address_id': x.address_id,
            'cereals': cereal,
            'price': total_price(OrderItems.objects.filter(order_id=x.id))
        }]
        cereal = []
    return render(request, 'user/order_history.html', {
        'orders': orders
    })


def search_history(request):
    """This function returns the search history of a user"""
    searches = [x.search_query for x in Search.objects.filter(user=request.user)]
    return render(request, 'user/search_history.html', {
        'searches': searches
    })
