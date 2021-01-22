from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    #url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
    path('about/', views.about,name='about')
    # ./templates/blog/post/home.html

    #url(r'^$', views.post_list, name='post_list'),
    #url(r'^(?P<pk>[0-9]+)/$',views.post_detail,name='post_detail'),
]
