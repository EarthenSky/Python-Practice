import PIL.Image

img = PIL.Image.open('cave.jpg')
width, height = img.size

out1 = img.convert('RGB')
out2 = img.convert('RGB')

pixels1 = out1.load()
pixels2 = out2.load()

save_px = (0, 0, 0)

for i in range(width):
    for j in range(0, height, 2):
        save_px = rgb_img.getpixel()
        pixels1[i, j] = (0, 0, 0) #Set the colour.
        #if (i + j) % 2 == 0:

        #else:
            pixels2[i, j] = (0, 0, 0) #Set the colour.

#-- Show images
out1.show()
out2.show()
