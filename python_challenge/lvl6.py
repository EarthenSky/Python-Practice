next_nothing = 90052

total = 0

out_main = ""

txt = "N"

_list = []

import zipfile
zip_thing = zipfile.ZipFile('channel.zip')
inf_list = zip_thing.infolist()

# Read from the txts.
while txt[0] == 'N':
    txt = ""

    old_nothing = next_nothing

    try:
        # Get txt file.
        fileObject = open("channel/{}.txt".format(next_nothing),'r')
        txt = fileObject.read()

        total += int(next_nothing)
        #total += str(txt)

        the_list = txt.split(" ")
        next_nothing = the_list[len(the_list)-1]

        _list.append( ( int(old_nothing), int(next_nothing) ) )

        for inf in inf_list:
            if inf.filename == "{}.txt".format(old_nothing):
                out_main += str(inf.comment)

    except:
        print txt
        print "errr"

    #if txt[0] == 'N':
    #print txt + "|" + str(old_nothing) + " -> " + str(next_nothing)
    #print str(( int(old_nothing), int(next_nothing) ))

print str(total)
print str(out_main)
#--------------------------------------
'''
last_num = 0
_list_2 = []
for x in range(99905):
    try:
        # Get txt file.
        fileObject = open("channel/{}.txt".format(x),'r')
        txt = fileObject.read()

        _list_2.append(x - last_num)

        last_num = x
    except:
        pass

'''
#---------------------------------------
'''
str_thing = str(total).replace("0", "a").replace("1", "b").replace("2", "c").replace("3", "d").replace("4", "e").replace("5", "f").replace("6", "g").replace("7", "h").replace("8", "i").replace("9", "j")
print str(str_thing)
'''
#---------------------------------------
'''
out_value = ""
for i in _list_2:
    out_value += str(i) + "|"

print str(out_value)
'''
#---------------------------------------

#print str(_list)

#---------------------------------------
#46145
#46293138
#46383190
#46337045
#1587818
#99775
#---------------------------------------
'''
import pygame, time

pygame.init()

#makes a screen of 1280 by 720
display_surface = pygame.display.set_mode( (1280, 1280) )

index = 0
last = 0
for x in range(len(_list_2)-1):

    pygame.draw.line(display_surface, (255, 100, 0, 255), (last/1, x*1),  (_list_2[index]/1, (x+1)*1), 1)
    last = _list_2[index]

    time.sleep(0.001)
    pygame.display.update() #updates displays
    index += 1

while True:
    print "hi"
'''
#---------------------------------------
'''
import urllib2, urllib

# Read from the website
x=0
for thing in _list:
    x+=1
    try:
        # Get page
        req = urllib2.Request('http://www.pythonchallenge.com/pc/def/{}.html'.format(thing))
        response = urllib2.urlopen(req)
        the_page = response.read()

        print the_page + "GOOOOD"
    except Exception as e:
        raise
'''
#---------------------------------------
'''
import wave, struct, math

sampleRate = 44100.0 # hertz
duration = 1.0       # seconds
frequency = 440.0    # hertz

wavef = wave.open('sound.wav','w')  # Write
wavef.setnchannels(1) # Mono
wavef.setsampwidth(2)
wavef.setframerate(sampleRate)

for value in _list:
    data = struct.pack('<h', int(value/3.049))
    wavef.writeframesraw( data )

wavef.writeframes('')
wavef.close()
'''
