from PIL import Image,ImageFont,ImageDraw

def add_num(in_file,num,out_file='result.jpg'):
    im = Image.open(in_file)
    font = ImageFont.truetype('C:/Windows/fonts/Arial.ttf',50)
    # fill_color = '#ff0000'
    fill_color = 'blue'
    draw = ImageDraw.ImageDraw(im)
    width,height = im.size
    print width,height
    draw.text((0,height-50),str(num),fill=fill_color,font=font)
    im.save(out_file)

add_num('p1.jpg',1)