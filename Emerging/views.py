from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('hello')

def intialco(request):
    return HttpResponse('Good')

def comp(request,co):
    return HttpResponse('Hi evryone page :')

# Create your views here.