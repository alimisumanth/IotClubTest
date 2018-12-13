from django.shortcuts import render


def homepage(request):
    # return HttpResponse("hello,world")
    return render(request, "homepage.html")


def corebody(request):
    # return HttpResponse("hello,world1")
    return render(request, "corebody.html")


def workshops(request):
    # return HttpResponse("hello,world1")
    return render(request, "workshops.html")


def course(request):
    # return HttpResponse("hello,world1")
    return render(request, "course.html")


def achievements(request):
    # return HttpResponse("hello,world1")
    return render(request, "achievements.html")


def index(request):
    # return HttpResponse("hello,world1")
    return render(request, "index.html")


def projects(request):
    # return HttpResponse("hello,world1")
    return render(request, "Projects.html")


def photo_gallery(request):
    # return HttpResponse("hello,world1")
    return render(request, "Photo Gallery.html")
