# encoding: utf-8
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect

class ContactForm(forms.Form):
    #联系我表单类,构建表单属性
    subject = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=20)
    sender = forms.EmailField()