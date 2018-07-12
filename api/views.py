from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from .bashScripts import pwd, countLines, fastText


def index(request):
    return HttpResponse("Hello, world. You're at the home page.")


def countlines(request):
    numlines = countLines()
    return render(request, 'api/bashResult.html', {'result': numlines})


def getcwd(request):
    cwd = pwd()
    return render(request, 'api/bashResult.html', {'result': cwd})


def fasttext(request):
    predictions = fastText()
    return render(request, 'api/bashResult.html', {'result': predictions})
