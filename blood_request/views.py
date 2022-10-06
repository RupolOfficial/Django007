from django.shortcuts import render, HttpResponse


# Create your views here.
def blood_request_views(request):
    return HttpResponse("<h1> This is Blood request page </h1>")
