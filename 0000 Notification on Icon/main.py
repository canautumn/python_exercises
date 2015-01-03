from PIL import Image, ImageFont, ImageDraw
import os

def add_number(im, num):
    fontsize = int(im.size[1] / 5)
    my_font = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.dfont", fontsize) # Font path for OS X
    my_draw = ImageDraw.Draw(im)
    stringsize = my_draw.textsize(str(num), my_font)
    my_draw.text((im.size[0] - stringsize[0], int(im.size[1]/50)), str(num), (255, 0, 0), font=my_font)
    
    return im
    
if __name__ == '__main__':
    filepath = "avatar.png"
    filename, fileext = os.path.splitext(filepath)
    number = 1000
    add_number(Image.open(filepath), number).save(filename + str(number) + fileext)

