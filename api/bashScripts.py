import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Function which takes in and executes unix commands and returns their output


def b(command):
    args = command.split(" | ")
    if len(args) == 0:
        return "please enter a unix command"
    elif len(args) == 1:
        p1 = subprocess.Popen(args[0], stdout=subprocess.PIPE)
        output = p1.communicate()[0].decode('utf-8')
        # print(output)
        return output
    else:
        p1 = subprocess.Popen(args[0], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(
            args[1].split(), stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        output = p2.communicate()[0].decode('utf-8')
        # print(output)
        return output


def pwd():
    directory = b('pwd')
    return directory


def countLines():
    numLines = b('ls | wc -l')
    return numLines


def ls():
    files = b('ls')
    return files


def fastText():
    os.chdir(MEDIA_ROOT)
    # build model
    b('fasttext supervised -input cooking.train -output model_cooking')
    # predictions
    predictions = b('fasttext predict model_cooking.bin cooking.valid')
    return predictions

    #b('fasttext test model_cooking.bin cooking.valid')
