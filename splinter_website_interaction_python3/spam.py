from splinter import Browser

name_list = []

# Website url
url = "https://travelsp.in/random"

browser = Browser('firefox')
browser.visit(url)

#for x in range(0, 500):

title = browser.find_by_xpath('html/body/div/div/div/div/h2')[1].click()
name_list.append(title)

print title

#browser.reload()



# browser.exit()

