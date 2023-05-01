from django.shortcuts import render

# Create your views here.
def pic(request):
    return render(request,'static_app/index.html',context={'image':'This is image'})