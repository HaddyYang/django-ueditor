#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response

def test(request):
    return render_to_response('ueTest.html')
