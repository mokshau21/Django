from django.urls import re_path
from first_template import views
urlpatterns=[
    re_path(r'^$',views.send_data,name="Data")
]