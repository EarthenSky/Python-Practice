import urllib2, urllib

all_str = ""
next_nothing = 8022

# Read from the website
for i in range(400):
    # Get page
    req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(next_nothing))
    response = urllib2.urlopen(req)
    the_page = response.read()

    the_list = the_page.split(" ")
    next_nothing = the_list[len(the_list)-1]
    #all_str += "|" + next_nothing
    print the_page + "|" + next_nothing

print all_str
