from django.shortcuts import render

from users.models import User
from users.froms import UserLoginForm


# Create your views here.
def login(request):
    context = {
        'form': UserLoginForm()
    }
    return render(request, 'users/login.html', context)


def registration(request):
    return render(request, 'users/registration.html')


def profile(request):
    return render(request, 'users/profile.html')
