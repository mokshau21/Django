from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from cbv_detail_list_view import models
# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'
class SchoolListView(ListView):
    template_name='cbv_detail_list_view/school_list.html'
    model=models.School
    context_object_name='schools'
class SchoolDetailView(DetailView):
    context_object_name='school_details'
    model=models.School
    template_name='cbv_detail_list_view/school_detail.html'