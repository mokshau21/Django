from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'filters_app/index.html',context={'text':"My name is Moksha","Num":100})