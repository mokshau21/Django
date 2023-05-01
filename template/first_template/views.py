from django.shortcuts import render

# Create your views here.
def send_data(request):
    m={'insert':"This is Moksha"}
    return render(request,'first_template/index.html',context=m)