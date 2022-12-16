from django.urls import re_path as url
from blog import views1

urlpatterns = [
    url(r'stroke', views1.stroke)
]