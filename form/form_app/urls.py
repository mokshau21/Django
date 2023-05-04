from django.urls import re_path
from form_app import views
urlpatterns=[
    re_path(r'^$',views.index,name="Moksha"),
             ]