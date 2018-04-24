import PIL.Image

img = PIL.Image.open('cave.jpg')
width, height = img.size

out1 = img.convert('RGB')
#out2 = img.convert('RGB')

pixels1 = out1.load()
#pixels2 = out2.load()

save_px = (0, 0, 0)

_img_list = []
_img_list2 = []

#Separate Imgs
count = 0
which = False
for y in range(height):
    for x in range(0, width, 1):
        save_px = out1.getpixel( (x, y) )
        pixels1[x, y] = save_px #Set the colour.
        if ((x + (y*count)) % 2) == 0:

            which = not which
            if which == True:
                _img_list.append(save_px)
            else:
                _img_list.append(save_px)

    count += 1

img2 = PIL.Image.new(img.mode, (int(width), int(height)))
img2.putdata(_img_list)

#-- Show images
#img2.show()

#img3 = PIL.Image.new(img.mode, (int(width/2), int(height/2)))
#img3.putdata(_img_list2)

#-- Show images
#img3.show()
#out2.show()

img2.save('img2.png')
