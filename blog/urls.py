from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    path('',views.post_list, name='post_list'),
    path('post/<int:post_id>', views.post_detail,name='post_detail'),
    #url(r'^(?P<pk>[0-9]+)/$',views.post_detail,name='post_detail'),
]
