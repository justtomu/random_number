import social_django.managers
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import ForeignKey
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor
from django.shortcuts import render, redirect
from django.http import HttpResponse
from icecream import ic
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth
from django.contrib.auth import logout as delete_user


def index(request: WSGIRequest):
    return HttpResponse('<h1>hello</h1>')


def logout(request):
    delete_user(request)
    return redirect('/')


def login(request):
    return render(request, 'login_page.html') if not request.user.is_authenticated else redirect('/get_number')


def get_number(request):
    return render(request, 'random_page.html') if request.user.is_authenticated else redirect('/')


def header(request):
    return render(request, 'header.html')
