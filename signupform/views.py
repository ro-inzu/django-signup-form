from django.shortcuts import render,redirect, get_object_or_404
from django import forms
from django.http import HttpResponse

# Create your views here.
def index(requests):

    return HttpResponse("Hello, world. You're at the signupform index.")
