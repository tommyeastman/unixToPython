from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .bashScripts import pwd, countLines, FT_predict, FT_train_predict


def index(request):
    return render(request, 'api/index.html')


def countlines(request):
    numlines = countLines()
    return render(request, 'api/bashResult.html', {'result': numlines})


def getcwd(request):
    cwd = pwd()
    return render(request, 'api/bashResult.html', {'result': cwd})


def fasttext(request):
    predictions = FT_train_predict()
    return render(request, 'api/bashResult.html', {'result': predictions})


def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        return render(request, 'api/BashResult.html', {'result': "File uploaded successfully"})
    return render(request, 'api/fileUpload.html')


# def generate_new_predictions(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         fs.save('data.valid', myfile)
#         predictions = FT_predict()
#         return render(request, 'api/BashResult.html', {'result': predictions})
#     return render(request, 'api/fileUpload.html')

def generate_new_predictions(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        predictions = FT_predict(myfile.name)
        return render(request, 'api/BashResult.html', {'result': predictions})
    return render(request, 'api/fileUpload.html')
