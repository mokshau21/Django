from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'template_inheritance_app/index.html')
def other(request):
    return render(request,'template_inheritance_app/other.html')
def relative(request):
    return render(request,'template_inheritance_app/relative.html')