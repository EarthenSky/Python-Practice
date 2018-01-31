import winsound  #for the beep sound
from time import sleep

#note to frequency dictionary (global)
g_notes = {
"A4" : 440,
"G#4" : 415,
"G4" : 392,
"F#4" : 370,
"F4" : 349,
"E4" : 330,
"D#4" : 311,
"D4" : 294,
"C#4" : 277,
"C4" : 262
}

# lists that hold the sound effect values
g_songnotelist = []
g_songlengthlist = []

#converts a note to a hz and plays sound for length (global)
def g_playSound(note, length):
    winsound.Beep(g_notes[note], length)

#checks if the character is a number or a string (global)
def g_isNumber(char):
    try:
        float(char)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(char)
        return True
    except (TypeError, ValueError):
        pass

    return False

#explanation of the program
print("This is a basic note sequencer,")
print("input each note followed by a number equaling the length of the note. (in ms)")
print("ex. C4 100 D4 100 D#3 100 \n")
print("Whitespace is ignored. \n")
print("The implemented notes & frequencies are: \n", g_notes, "\n")

noteinput = input("Input: ")  #request input
noteinput = noteinput.replace(" ", "")  #remove whitespace

parsestage = 0  #holds current stage of parsing

#init note values
noteval = ""
notelength = ""

#parse stages check if the current character being parsed is correct
def parseStageOne(char):
    global noteval, parsestage
    if(g_isNumber(char) == False):
        parsestage = 1  #next parse stage is number or # for note
        noteval += char  #use the value
    else:
        print("ERR:1, this char : (", char ,") is supposed to be a letter for note")
def parseStageTwo(char):
    global noteval, parsestage
    if(g_isNumber(char) == True):
        parsestage = 3  #next parse stage is number for length
        noteval += char  #use the value
    elif(char == '#'):
        parsestage = 2  #next parse stage is number for note
        noteval += char  #use the value
    else:
        print("ERR:2, this char : (", char ,") is supposed to be a number or a # for note")
def parseStageThree(char):
    global noteval, parsestage
    if(g_isNumber(char) == True):
        parsestage = 3  #next parse stage is number for length
        noteval += char
    else:
        print("ERR:3, this char : (", char ,")  is supposed to be a number for note")
def parseStageFour(char):
    global noteval, notelength
    if(g_isNumber(char) == True):
        notelength += char
    else:
        #add values to list
        g_songnotelist.append(noteval)
        g_songlengthlist.append(notelength)

        print("noteval is: ", noteval)

        #reset values for next note
        noteval = ""
        notelength = ""

        #start at stage one again
        parseStageOne(char)

print(noteinput)
print(len(noteinput))

#loop once for each character
for i in range(len(noteinput)):
    currentchar = noteinput[i]  #get the char that is being parsed
    print(currentchar)

    #choose parse stage
    if(parsestage == 0):
        parseStageOne(currentchar)
    elif(parsestage == 1):
        parseStageTwo(currentchar)
    elif(parsestage == 2):
        parseStageThree(currentchar)
    elif(parsestage == 3):
        parseStageFour(currentchar)
    else:
        print("ERR:0, this is not supposed to be called.")


#add last values to list
g_songnotelist.append(noteval)
g_songlengthlist.append(notelength)

# play indexed sounds in order
for i in range(len(g_songnotelist)):
    g_playSound(g_songnotelist[i], int(int(g_songlengthlist[i])/2))
    sleep(int(g_songlengthlist[i])/2000)

#wait 1 second
sleep(0.5)

# completed melody
g_playSound("G#4", 200)
g_playSound("G#4", 50)
g_playSound("G#4", 50)
g_playSound("A4", 200)

print("dekimashita!")  #I did it!

# a basic melody:
# slow one   : F4 500 F4 500 E4 500 E4 500 D4 500 D4 500 C4 500 C4 500
# dynamic    : A4 250 A4 250 G4 125 A4 250 E4 250 C4 250 D4 250 C4 125 C#4 125 D4 125
# sweep down : A4 250 G#4 250 G4 250 F#4 250 F4 250 E4 250 D#4 250 D4 250 C#4 250 C4 250
# coin       : C4 150 A4 450
