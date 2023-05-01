from django.urls import re_path
from static_app import views
urlpatterns=[
    re_path(r'^$',views.pic,name='name')
]