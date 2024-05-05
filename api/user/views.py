
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout




def login(request):
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')





