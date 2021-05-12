from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test

from cart.views import get_cart
from cereal.forms.cereal_form import CerealCreateForm, CerealUpdateForm
from cereal.models import Cereal, CerealImage, CerealCategory
from user.models import Search
from datetime import datetime
from django.core import serializers
import json

# Create your views here.


def cereal_objects_to_json(cereals_obj):
    """Helper function to turn cereal objects into json."""
    cereals = [{
        'id': x.id,
        'name': x.name,
        'image': x.cerealimage_set.first().image,
        'price': x.price,
        'sugar': x.sugar
    } for x in cereals_obj]
    return cereals


def cereal_catalog(request):
    """Testing a different approach"""
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']

        # If an authorized user is searching, his search query is saved to the database
        if search_filter != "":
            if request.user.is_authenticated:
                new_search_entry = Search(search_query=search_filter, search_date=datetime.now(), user=request.user)
                new_search_entry.save()

        order_by = request.GET['order_by']

        filter_str = request.GET['filters']
        if filter_str == '':
            filters = CerealCategory.objects.all()
        else:
            filters = filter_str.split(',')

        cereals = cereal_objects_to_json(
            Cereal.objects.filter(
                category__in=filters,
                name__icontains=search_filter
            ).order_by(order_by)
        )

        # Makes sure there are no duplicates, this could probably be done in the query
        unique_cereals = []
        for cereal in cereals:
            if cereal not in unique_cereals:
                unique_cereals.append(cereal)
        cereals = unique_cereals

        return JsonResponse({'data': cereals})

    if 'search_history' in request.GET:
        searches = [{'search_query': search.search_query} for search in Search.objects.filter(user=request.user)]
        searches.reverse()
        return JsonResponse({'data': searches[:6]})

    # What is returned when there is no query in the url
    # If the user is authenticated, his search history is returned along with the cereals and categories
    context = {
        'cereals': Cereal.objects.all().order_by('name'),
        'categories': CerealCategory.objects.all(),
    }

    if request.user.is_authenticated:
        cart_json = get_cart(request)
        cart_obj = json.loads(cart_json.content)
        context['data'] = cart_obj['data']
        searches = [{'search_query': y.search_query} for y in Search.objects.filter(user=request.user)]
        searches.reverse()
        context['searches'] = searches[:6]
        return render(request, 'cereal/index.html', context)
    # If user is not authenticated, only categories and cereals are returned
    else:
        return render(request, 'cereal/index.html', context)


def get_cereal_by_id(request, id):
    """ This function renders the cereal details page of a clicked cereal on the catalog."""
    if request.method == 'POST':
        if request.POST.get('quantity') == '':
            quantity = 1
        else:
            quantity = request.POST.get('quantity', default=1)

        if request.POST['buyproduct'] == 'Buy now':
            return redirect('buy-single-item', cereal_id=id, quantity=quantity)
        else:
            return redirect('add-to-cart', cereal_id=id, quantity=quantity)
    context = {
        'cereal': get_object_or_404(Cereal, pk=id)
    }
    if request.user.is_authenticated:
        cart_json = get_cart(request)
        cart_obj = json.loads(cart_json.content)
        context['data'] = cart_obj['data']
    return render(request, 'cereal/cereal_details.html', context)


@user_passes_test(lambda u: u.is_superuser)
def create_cereal(request):
    """This function renders a form for creating a new cereal, and saves it to the database.
    Only a superuser can create a new cereal."""
    # A POST request will save the new cereal to the database.
    if request.method == 'POST':
        form = CerealCreateForm(data=request.POST)
        if form.is_valid():
            cereal = form.save()
            cereal_image = CerealImage(image=request.POST['image'], cereal=cereal)
            cereal_image.save()
            return redirect('cereal-index')
    # If not a POST request a page is rendered for filling in information about a new cereal.
    else:
        form = CerealCreateForm()
        return render(request, 'cereal/create_cereal.html', {
            'form': form
        })


@user_passes_test(lambda u: u.is_superuser)
def delete_cereal(request, id):
    """This function deletes an existing cereal from the database.
    Only a superuser can perform this task."""
    cereal = get_object_or_404(Cereal, pk=id)
    cereal.delete()
    return redirect('cereal-index')


@user_passes_test(lambda u: u.is_superuser)
def update_cereal(request, id):
    """This function updates an existing cereal in the database.
    Only a superuser can perform this task."""
    instance = get_object_or_404(Cereal, pk=id)
    if request.method == 'POST':
        form = CerealUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('cereal-details', id=id)
    else:
        form = CerealUpdateForm(instance=instance)
    return render(request, 'cereal/update_cereal.html', {
        'form': form,
        'id': id
    })
