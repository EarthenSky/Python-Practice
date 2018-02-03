import string
import re  # Regular expressions

# Find the paragraph file
text_file = open("paragraph.txt", "r")

# Get the text string from the file
paragraph = text_file.read()

# Create list of the words in the file
words = paragraph.split(" ")

dict = {}

# Loop through each item in the words list
for word in words:
    # Remove punctuation and capitalization and all (\n)s
    word = word.translate(None, string.punctuation).lower()
    word = re.sub(r"\s+", "", word)
    
    # Count amount of words and add them to the dictionary
    if(word in dict):
        dict[word] += 1
    else:
        if(word != " " and word != ""):
            dict[word] = 1

print "This is a list of how many times each word appears. \n"

# Sort & Output Values
for key, value in sorted(dict.iteritems(), key=lambda (k,v): (v,k)):
    print "{} : {}".format(key, value)
