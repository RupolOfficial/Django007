from django.shortcuts import render, HttpResponse


# Create your views here.
def contact_views(request):
    return HttpResponse("<h1> This is contact page </h1>")
