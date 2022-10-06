from django.shortcuts import render, HttpResponse


# Create your views here.
def donor_views(request):
    return HttpResponse("<h1> This is donor page </h1>")
