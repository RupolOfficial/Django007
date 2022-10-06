from django.shortcuts import render, HttpResponse


# Create your views here.
def about_views(request):
    return render(request,'about.html')
