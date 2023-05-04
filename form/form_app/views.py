from django.shortcuts import render
from django.http import HttpResponse
from form_app import forms
# Create your views here.
def index(request):
    f=forms.FormName()
    if request.method=='POST':
        f=forms.FormName(request.POST)
        if f.is_valid():
            print("form validation is done")
            print('Name: '+f.cleaned_data['name'])
            print('Email: '+f.cleaned_data['email'])
            print('Text: '+f.cleaned_data['email'])
    return render(request,'form_app/index.html',{'forms1':f})
