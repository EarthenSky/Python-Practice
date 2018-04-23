g_un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
g_p = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

#print('\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00'.decode('iso-8859-1'))
#print(g_p.decode('iso-8859-1'))
#print("\xe2\x82\x80")

#file_object = open("file.txt", "w")
#file_object.write(g_un + "|||" + g_p)
import zlib, bz2

decompressor = bz2.BZ2Decompressor()

#print decompressor.decompress(g_un)
print decompressor.decompress(g_un)
#y = gzip.compress(b'0sfg^sdfgcoetohDabyss.')
#print( y.split(b" ") )
#x = gzip.decompress(g_p)
#y = zlib.decompress(g_p)

#import pyperclip
#pyperclip.copy('\x00')
#spam = pyperclip.paste()


# FUCK YOU COMPRESSION

# ok, sorry compression.
