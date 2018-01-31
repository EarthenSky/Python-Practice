import winsound
import random

def getRandomTone():
    #generates a random tone between 200 and 20000
    return random.randint(20, 200) * 10

def annoy():
    for i in range(1, 100):
        winsound.Beep(getRandomTone(), 100)

annoy();
