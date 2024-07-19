from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact2(request):
    return render(request, "contact2.html")


def spotify(request):
    return render(request, "spotify.html")