import PIL.Image

img = PIL.Image.open('oxygen.png')
rgb_img = img.convert('RGB')

# Makes a list of all of the rgb greyscale values of the pixels
out_list = []
for i in range(0, 87):
    r, g, b = rgb_img.getpixel((i * 7, 48))
    out_list.append(chr(r))

print( str(out_list) )

#----------------------------------
