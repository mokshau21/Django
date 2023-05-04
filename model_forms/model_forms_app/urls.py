from django.urls import re_path
from model_forms_app.views import index
urlpatterns=[
    re_path(r'^$',index,name='index'),
]