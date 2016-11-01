#coding:utf-8
from django.conf.urls import include, url
from .controller import handler
import os

ueditor_path = os.path.join(os.path.dirname(__file__), "UE")

urlpatterns = [
    url(r'^$', handler),
    url( r'^UE/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': ueditor_path }),
]
