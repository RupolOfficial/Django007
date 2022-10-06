from django.shortcuts import render, HttpResponse


# Create your views here.
def find_donor_views(request):
    return HttpResponse("<h1> This is find donor page </h1>")
