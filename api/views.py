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

# Generate predictions with new data and pre-trained cooking model


def generate_new_predictions(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        predictions = FT_predict(myfile.name)
        return render(request, 'api/BashResult.html', {'result': predictions})
    return render(request, 'api/generatePredictions.html')

# Train new fastText classification model and generate predictions


def fasttext(request):
    modelData = 'cooking.txt'
    validationData = 'cooking.val'
    if request.method == 'POST':
        modelDataFile = request.FILES['modelDataFile']
        validationDataFile = request.FILES['validationDataFile']
        fs = FileSystemStorage()
        fs.save(modelDataFile.name, modelDataFile)
        fs.save(validationDataFile.name, validationDataFile)
        modelData = modelDataFile.name
        validationData = validationDataFile.name
        predictions = FT_train_predict(modelData, validationData)
        return render(request, 'api/bashResult.html', {'result': predictions})
    return render(request, 'api/fastText.html')
