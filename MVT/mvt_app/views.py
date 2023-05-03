from django.shortcuts import render
from django.http import HttpResponse
from mvt_app.models import Topic,Webpage,AccessRecord
# Create your views here.
def main_page(request):
    return HttpResponse("This is moksha")
def index(request):
    web_page=AccessRecord.objects.order_by('date')
    date_dict={'access_records':web_page}
    return render(request,'mvt_app/index.html',context=date_dict)