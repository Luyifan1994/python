# coding:utf-8
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw,ImageFilter

import random,numpy,string

def randstr():
    field = string.letters + string.digits
    text = random.sample(field,1)[0]
    return text

def randcolor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def randcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# print randcolor1,randcolor2

width = 60 * 4
height = 60
im = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draw(im)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=randcolor1())

for t in range(4):
    draw.text((60*t+20,10),randstr(),font=font,fill=randcolor2())

im = im.filter(ImageFilter.BLUR)
im.save('checkcode.jpg')