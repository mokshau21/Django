from django.urls import re_path
from template_relative_url_app import views
app_name='template_relative_url_app'
urlpatterns=[
    re_path(r'^relative/$',views.relative_url_template,name="relative"),
    re_path(r'^other/$',views.other,name='other')
]