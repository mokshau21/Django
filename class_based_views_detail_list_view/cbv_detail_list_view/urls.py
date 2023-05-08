from django.urls import re_path
from cbv_detail_list_view import views
app_name='app'
urlpatterns=[
    re_path(r'^$',views.SchoolListView.as_view(),name='list'),
    re_path(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail')
]