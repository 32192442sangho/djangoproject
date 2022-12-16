from django.urls import re_path as url

from dlearn import fashion_view

urlpatterns = [
    url(r'get/fashion/(?P<testNum>)$', fashion_view.find_error),
    url(r'post/fashion', fashion_view.find_fashion)
]