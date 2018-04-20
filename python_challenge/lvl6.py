next_nothing = 90052

total = ""

txt = "N"

_list = []

# Read from the website
while txt[0] == 'N':
    txt = ""

    old_nothing = next_nothing

    try:
        # Get txt file.
        fileObject = open("channel/{}.txt".format(next_nothing),'r')
        txt = fileObject.read()

        total += str(next_nothing)

        the_list = txt.split(" ")
        next_nothing = the_list[len(the_list)-1]

        _list.append( int(old_nothing) )

    except:
        print txt
        print "errr"

    #if txt[0] == 'N':
    print txt + "|" + str(old_nothing) + " -> " + str(next_nothing)

print str(total)

str_thing = str(total).replace("0", "a").replace("1", "b").replace("2", "c").replace("3", "d").replace("4", "e").replace("5", "f").replace("6", "g").replace("7", "h").replace("8", "i").replace("9", "j")
print str(str_thing)
'''
out_chars = ""
for num in _list:
    out_chars += chr(num)
'''

print str(_list)

'''
#46145
#46383190
#46383190

import pygame, time

pygame.init()

#makes a screen of 1280 by 720
display_surface = pygame.display.set_mode( (1280, 1280) )

index = 0
for x in range(len(_list)-1):
    pygame.draw.circle(display_surface, (255 - int(index/len(_list)*255.0*100), int(index/len(_list)*255.0*100), 0, 255), _list[index], 3, 0)
    time.sleep(0.001)
    pygame.display.update() #updates displays
    index += 1

while True:
    print "hi"
'''
