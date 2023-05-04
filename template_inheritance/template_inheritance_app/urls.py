from django.urls import re_path
from template_inheritance_app import views
app_name='app'
urlpatterns=[
    re_path(r'^other/',views.other,name='other'),
    re_path(r'^relative/',views.relative,name='relative')
]