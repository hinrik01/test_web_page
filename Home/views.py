from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect("cereal-index")
    else:
        return render(request, 'Home/index.html')


def about_us(request):
    return render(request, 'Home/about_us.html')


def contact(request):
    return render(request, 'Home/contact.html')


def privacy_policy(request):
    return render(request, 'Home/privacy_policy.html')


def terms(request):
    return render(request, 'Home/terms.html')
