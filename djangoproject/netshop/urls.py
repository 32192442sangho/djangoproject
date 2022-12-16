from django.urls import re_path as url

from netshop import iris_view

urlpatterns = [
    url(r'iris', iris_view.find_iris)
]