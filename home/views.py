from django.shortcuts import render
from django.http import HttpResponse
from templates import *


# Create your views here.

def home(request):
    return render(request, 'index.html', {})


def post(request):
    return render(request, 'post.html', {})


def posts(request):
    return render(request, 'posts.html', {})


def profile(request):
    return render(request, 'profile.html', {})


def contact(request):
    return render(request, 'contact_form.html', {})
