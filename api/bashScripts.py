import os
import subprocess


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


def fastText():
    os.chdir("C:\\Users\\abc\\Documents\\Redshred\\fastText-0.1.0")
    # build model
    b('fasttext supervised -input cooking.train -output model_cooking')
    #b('fasttext test model_cooking.bin cooking.valid')
    # predictions
    predictions = b('fasttext predict model_cooking.bin cooking.valid')
    return predictions
