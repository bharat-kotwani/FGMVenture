"""
Definition of views.
"""

from django.shortcuts import render,render_to_response
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    return render_to_response('index.html',{})

def contact(request):
    return render_to_response('contact.html',{})


def about(request):
    return render_to_response('about.html',{})

def blog(request):
    return render_to_response('blog.html',{})

def loanproject(request):
    return render_to_response('projectloan.html',{})

