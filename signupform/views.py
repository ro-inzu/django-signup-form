from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PostForm
import requests

# Create your views here.
def index(request):
    print('--views: index--')
    #render() fnc will put together the template under /appname/templates
    initial={'first_name': request.session.get('first_name', 'first name')}
    initial={'last_name': request.session.get('last_name', 'last name')}
    initial={'mobile_number': request.session.get('mobile_number', None)}


    form = PostForm(request.POST or None, initial=initial)
    if request.method == "POST":
        print('--views: index [form submitted]--')
        print(form)
        if form.is_valid():
            print('form is valid')
            request.session['first_name'] = form.cleaned_data['first_name']
            request.session['last_name'] = form.cleaned_data['last_name']
            request.session['mobile_number'] = form.cleaned_data['mobile_number']

            signup_info_list = []
            first_name = request.session['first_name']
            last_name = request.session['last_name']
            mobile_number = request.session['mobile_number']

            signup_info_list.append(first_name)
            signup_info_list.append(last_name)
            signup_info_list.append(mobile_number)
            print('first name: {}\n last name: {}\n mobile: {}'.format(first_name,last_name,mobile_number))

            return render(request,'signupform/confirmation.html',{'form':form,'signup_info_list':signup_info_list})
    else:
        form = PostForm()

    return render(request,'signupform/form.html',{'form':form})
