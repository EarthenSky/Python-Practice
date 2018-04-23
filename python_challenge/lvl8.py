g_un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
g_p = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(g_un)
print(g_p)

print("\xe2\x82\x80")

file_object = open("file.txt", "w")
file_object.write(g_un + "|||" + g_p)

#import pyperclip
#pyperclip.copy('\x00')
#spam = pyperclip.paste()
