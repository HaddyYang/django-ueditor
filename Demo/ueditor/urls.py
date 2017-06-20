#coding:utf-8
from django.conf.urls import include, url
from django.views.static import serve
from .controller import handler
import os

ueditor_path = os.path.join(os.path.dirname(__file__), "UE")

urlpatterns = [
    url(r'^$', handler),
    url( r'^UE/(?P<path>.*)$', serve, {'document_root': ueditor_path}),
]
