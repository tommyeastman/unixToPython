import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Function which takes in and executes unix commands and returns their output


def b(command):
    args = command.split(" | ")
    if len(args) == 0:
        return "please enter a unix command"
    # No piping
    elif len(args) == 1:
        p1 = subprocess.Popen(args[0], stdout=subprocess.PIPE)
        output = p1.communicate()[0].decode('utf-8')
        return output
    # Piping
    else:
        p1 = subprocess.Popen(args[0], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(
            args[1].split(), stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        output = p2.communicate()[0].decode('utf-8')
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

# Generate predictions from .txt using pre-trained cooking model


def FT_predict(validationData):
    predictions = b(
        f'fasttext predict {MEDIA_ROOT}/cooking_model.bin {MEDIA_ROOT}/{validationData}')
    return predictions

# Generate predictions from string using pre-trained cooking model


def FT_predict_string(string):
    # Create new .txt file and write contents of textbox to file
    b(f'touch {MEDIA_ROOT}/newFile.txt')
    text_file = open(f'{MEDIA_ROOT}/newFile.txt', 'w')
    text_file.write(string)
    text_file.close()
    # Read file into fastText to create predictions
    predictions = b(
        f'fasttext predict {MEDIA_ROOT}/cooking_model.bin {MEDIA_ROOT}/newFile.txt')
    b(f'rm {MEDIA_ROOT}/newFile.txt')
    return predictions

# Train new fastText classification model and generate predictions


def FT_train_predict(trainingData, validationData):
    # build model
    b(f'fasttext supervised -input {MEDIA_ROOT}/{trainingData} -output {MEDIA_ROOT}/model')
    # generate predictions
    predictions = b(
        f'fasttext predict {MEDIA_ROOT}/model.bin {MEDIA_ROOT}/{validationData}')
    return predictions
