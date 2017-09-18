# coding: utf-8
# 使用 Python 生成字母验证码图片

import string,random
from PIL import Image,ImageFont,ImageDraw

def getrandchar():
	return [random.sample(string.letters,4))]
	
def getrandcolor():
	return (random.ra)