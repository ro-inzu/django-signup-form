from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    hello = 'hello'

    return render(request,'signupform/form.html',{})
