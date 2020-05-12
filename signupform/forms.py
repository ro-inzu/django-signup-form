#-*- coding: utf-8 -*-
from django import forms

class PostForm(forms.Form):
    first_name = forms.CharField(label='first_name',empty_value='first name')
    last_name = forms.CharField(label='last_name',empty_value='last name')
    mobile_number = forms.CharField(label='mobile_number')
