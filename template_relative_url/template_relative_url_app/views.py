from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'template_relative_url_app/index.html')
def base(request):
    return render(request,'template_relative_url_app/base.html')
def other(request):
    return render(request,'template_relative_url_app/other.html')
def relative_url_template(request):
    return render(request,'template_relative_url_app/relative_url_template.html')