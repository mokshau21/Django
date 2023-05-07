from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class IndexView(TemplateView):
    template_name='cbv_templates/index.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']="This is injected comment"
        return context
