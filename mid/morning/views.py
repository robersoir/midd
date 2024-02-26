from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    return HttpResponse('home page')
def about(request):
    return HttpResponse('about page')
def contact(request):
    return HttpResponse('contact us')