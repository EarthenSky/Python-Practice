import urllib2

# Website url
url = "https://travelsp.in/random"
url2 = "https://travelsp.in/"

HEADERS = {'User-Agent': 'Mozilla/5.0'}

name_list = []

#for index in range(100):
# Get the page text
request = urllib2.Request(url2, headers=HEADERS)
response = urllib2.urlopen(request)
the_page = response.read()

index = the_page.find("destination.title")

title = the_page[index:index+50]

print the_page

#name_list.append()

print name_list
