import random

def read_text(file_name):
    file_data = []
    text_file = open(file_name,"r")

    for word in text_file.read().split():
        file_data.append(word)

    text_file.close()
    return file_data

def getWord():
    list = read_text("words.txt")
    return random.choice(list)
