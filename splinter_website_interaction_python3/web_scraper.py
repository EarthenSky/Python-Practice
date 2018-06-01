# -*- coding: cp1252 -*-
from splinter import Browser
import time

test_string = "SAN JOSÉ"

with open("places_list.txt", "a", encoding='utf-8') as file:
    file.write(test_string)


name_list = []

# Website url
url = "https://travelsp.in/random"

browser = Browser('firefox')

print( "SEARCHING" )

for index in range(0, 1000):
    browser.visit(url)  # Random Page

    time.sleep(1)  # Wait for page to load.
    
    # Find title.
    title_element = browser.find_by_xpath('/html/body/div/div/div/div/h2').first
    
    #print( title_element.text )
    print( index )
    
    name_list.append(title_element.text)

print( "WRITING" )

with open("places_list.txt", "a",encoding='utf-8') as file:
    for name_string in name_list:
        file.write(name_string + '|')

print( "DONE" )

#browser.reload()

# browser.exit()

