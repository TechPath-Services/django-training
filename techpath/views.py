from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "home.html")

def myfile(request):
    return render(request, "myfile.html")

def contact2(request):
    return render(request, "contact2.html")


def spotify(request):
    return render(request, "spotify.html")

