## Overview

This is a Django web app to run any Unix script in the browser.

A few Unix commands are used to show as examples of what is possible:
- `pwd`
- `ls | wc -l`

The app handles piping of Unix commands, i.e. in the example above, `ls | wc -l`

The purpose of the app is to be able to create a frontend for any machine learning package that is released in Unix.

The app is not deployed and sits locally. I use a local .sqlite3 database and the Django dev server. When you run the server, you can interact with the app in your local port.

## Run App

Simply clone the repo, cd into the unixPython2 directory, and run

`python manage.py runserver`

Then type this url into your browser

http://localhost:8000/api/

## FastText

I've used fastText for this app as an example of the machine learning package binding functionality, as
fastText was released originally in Unix without any Python bindings.  All calls to fastText methods are using only Unix.

I trained a fastText supervised learning model using data from the cooking section of StackExchange, following along with [the official tutorial](https://fasttext.cc/docs/en/supervised-tutorial.html)

### Functionality
1. Generate new predictions for a pre-trained fastText classification model from a .txt file

User uploads .txt file with a list of sentences and the cooking model generates a label for each sentence

2. Generate new predictions for a pre-trained fastText classification model by typing

User types sentences into a textbox and the cooking model generates a label for each sentence

3. Train a fastText classification model and generate predictions for the validation set

User uploads labeled data to train a new model with, along with a .txt file with a list of sentences. A new fastText model is trained on the data and the model generates a label for each sentence

## How it Works
As part of the standard Django layout, each URL corresponds to a View, a python function that runs other functions and tells the browser what to render.

Most of the logic of the app exists in **bashScripts.py**. This contains a python function I created, b(), to parse the Unix command and execute the command in python. Each view calls a separate function in bashScripts.py and those functions may make several calls to b().

The app handles file uploading using standard Django functionality. All uploaded files are stored at /media. The files are grabbed directly from the POST request.

In the case of #1 and #3 from the fastText functionality listed above, the unix command string is simply passed in the .txt filename using python fstring syntax. In the case of #2, a .txt file is created using Unix, the content of the text input is placed into the file using Python, the model is created using Unix, and the file is then deleted using Unix.