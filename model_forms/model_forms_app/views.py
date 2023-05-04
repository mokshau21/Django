from django.shortcuts import render
from model_forms_app.forms import FormName
# Create your views here.
def index(request):
    return render(request,'model_forms_app/index.html')
def formpage(request):
    f=FormName()
    if request.method=='POST':
        f=FormName(request.POST)
        if f.is_valid():
            print("First Name: ",f.cleaned_data['first_name'])
            print("Last Name: ",f.cleaned_data['last_name'])
            print("Email: ",f.cleaned_data['email'])
            f.save()
            return index(request)
    return render(request,'model_forms_app/form.html',context={'form':f})