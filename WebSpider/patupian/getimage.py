#--*-- coding:utf-8 --*--
import os
import urllib
import re

url = r"http://www.u148.net/article/37161.html"

def gethtml(url):
	file = urllib.urlopen(url)
	html = file.read()
	return html
	
def getimg(html):
	reg = r'src="(.+?scenery.+?\.jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	# print imglist
	return imglist
	
def download(imglist):
	x = 1
	for img in imglist:
		urllib.urlretrieve(img,r'C:\Work\python\patupian\Image\%d.jpg' %x)
		x+=1

def main():
	# os.system('mkdir Image')
	# print 'enter web page:'
	# url = raw_input()
	html = gethtml(url)
	imglist = getimg(html)
	download(imglist)

main()