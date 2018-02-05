# Regular expressions are simple pattern finding algorithms that can
# be mashed together to look for special things in strings.
# Regular expressions are almost their own programming language.
import re
import string
import urllib  # This Lets you read from websites
from PIL import Image  # This lets me create imgs
import collections  # Ordered dictionary
import os.path  # For checking file names

# Finds the paragraphs in a standard wikipedia page
def get_paragraphs(paragraph):
    return paragraph #TODO: this

# These falgs indicate what the goal of the program is
f_websearch = False
f_filesearch = False
f_defaultfile = False

# Init statements
print "This prorgam sorts text by words and their occurance."
print "To sort a website, press : 0"
print "To sort a file,    press : 1"
 
# Query user input with an elif statement in a while loop
valid_input = False
while valid_input == False:
    
    input_string = raw_input("Input: ")

    if input_string == "0":
        valid_input = True
        f_websearch = True
        
    elif input_string == "1":
        valid_input = True
        f_filesearch = True
        
    else:
        print "Invalid input, please type 1 or 0."

# This is the sting that holds all of the paragraph text
paragraph = ""

# This is the path for the website or the filename
path = ""

if f_websearch == True:
    valid_input = False  
    while valid_input == False:
        try:
            path = raw_input('Input a website adress (try https://en.wikipedia.org/wiki/Special:Random): ')

            website = urllib.urlopen(path)

            # Get the website's code 
            paragraph = website.read()

            print "Please type 1 for converted website or 0 for un-converted."
            print '"Converted" just means only paragraphs are targeted although the algorithmn is pretty crude.'
            print 'Converted websites are currently unsupported and will default to un-converted.'
            
            valid_input2 = False
            while valid_input2 == False:
    
                input_string = raw_input("Input: ")

                if input_string == "0":
                    valid_input2 = True
    
                elif input_string == "1":
                    valid_input2 = True
                    paragraph = get_paragraphs(paragraph)
        
                else:
                    print "Invalid input, please type 1 or 0."

            
            valid_input = True

        except IOError:
            print "Oops!  That was not a valid website adress.  Try again... \n"
    
elif f_filesearch == True:
    valid_input = False  
    while valid_input == False:
        try:
            path = raw_input('Input a file name, or "def" for the default file: ')

            if path.strip() == "def":
                path = "paragraph.txt"
                text_file = open(path, "r")
            
            else:
                text_file = open(path, "r")

            # Get the text string from the file
            paragraph = text_file.read()
            
            valid_input = True

        except IOError:
            print "Oops!  That was not a valid filename.  Try again... \n"
    

# Replace newline with space
paragraph = paragraph.replace("\n", " ")

# Create list of the words in the file
words = paragraph.split(" ")

dict = {} 

# Loop through each item in the words list
for word in words:
    # Remove punctuation and capitalization and all (\n)s
    word = word.translate(None, string.punctuation).lower()
    word = re.sub(r"\s+", "", word)

    # Count amount of words and add them to the dictionary
    if word in dict:
        dict[word] += 1
    else:
        if(word != " " and word != ""):
            dict[word] = 1

print "This is a list of how many times each word appears. \n"

# This is for building the graph.
# This dictionary remembers the order of the keys.
dict2 = collections.OrderedDict()

# Sort & Output Values
for key, value in sorted(dict.iteritems(), key=lambda (k,v): (v,k)):
    print "{} : {}".format(key, value)
    dict2[key] = value

    
print "\n Total words : {}".format(len(dict2))

print "Create graph? (xAxis is wordname, yAxis is wordcount)"

valid_input2 = False
while valid_input2 == False:
    
    input_string = raw_input("Input y/n: ")

    if input_string == "n":
        valid_input2 = True
    
    elif input_string == "y":
        valid_input2 = True
        
    else:
        print "Invalid input, please type y or n."

# Creates a graph
if input_string == "y": 
    width = 6400
    height = 6400
    
    img = Image.new('RGB', (width, height))

    pixels = img.load()

    # How many pixels each element takes up
    pixel_to_bar_value = float(width) / len(dict)
    # Multiply the value of a bar by this to get the px height
    value_to_px_height_mod = 640 / dict2.items()[len(dict2)-1][1]
    # How much the pixel overflows the current bar
    pixel_overflow = 0
    current_dict_index = -1
    
    for x in range(width-1):

        print current_dict_index
        
        y = height
        bar_top = 0

        avg_divisor = 0
        bar_height_sum = 0
        til_one = pixel_overflow

        #avg_divisor += 1
        #bar_height_sum += dict[current_dict_index]
        #if til_one > 1:
        #    pass
        #else:
        #    til_one += pixel_to_bar_value

        if til_one >= 1:
            avg_divisor += 1
            bar_height_sum += dict2.items()[current_dict_index][1]
            
        while til_one < 1:
            
            current_dict_index += 1
            avg_divisor += 1

            #print str(til_one) + " h " + str(current_dict_index)
            
            bar_height_sum += dict2.items()[current_dict_index][1]

            til_one += pixel_to_bar_value
            
            
        # Create next overflow value
        if til_one - 1 > 0:
            pixel_overflow = til_one - 1
            #bar_height_sum *= 1/til_one
        else:
            pixel_overflow = 0

        # Calculate the bar top
        bar_top = (bar_height_sum / avg_divisor) * value_to_px_height_mod

        # Place pixels until the top of the current bar is reached        
        while y > height - bar_top:
            y -= 1
            pixels[x, y] = (255, int(x/6), int(x/3))

    filename_index = 0

    # This makes sure each file has a unique name
    while os.path.isfile("{}_graph.png".format(filename_index)) == True:
        filename_index += 1
        
    img.save("{}_graph.png".format(filename_index))
    

print "Program complete!"
