import PIL.Image

img = PIL.Image.open('oxygen.png')
rgb_img = img.convert('RGB')

# Makes a list of all of the rgb greyscale values of the pixels
out_list = ""
for i in range(0, 87):
    r, g, b = rgb_img.getpixel((i * 7, 48))
    out_list += chr(r)

print( str(out_list) )

_next = [105, 110, 116, 101, 103, 114, 105, 116, 121]

out = ""
for num in _next:
    out += chr(num)

print(out)

#----------------------------------
