# 1024*768

import os,Image,glob
rootdic = r'C:\Work\python\chicun\image'
targetDir = r'C:\Work\python\chicun\overimage'
# print glob.glob(rootdic+r'\*.jpg')[0].split("\\")[-1]

def judgesize(img):
	imgsize = img.size
	if max(imgsize) > 1024:
		return True
	else:
		return False

def changesize(img):
	maxvalue = 0
	minvalue = 0
	maxvalue = max(img.size)
	minvalue = min(img.size)
	# print maxvalue,minvalue
	# times = maxvalue/1024
	# minvalue = minvalue/times
	newimg = img.resize((1024,768),Image.ANTIALIAS)
	return newimg

def main():
	for filename in glob.glob(rootdic+r'\*.jpg'):
		imgname = filename.split('\\')[-1]
		img = Image.open(filename,'r')
		if (judgesize(img) == True):
			newimg = changesize(img)
			newimg.save(targetDir+r'\\'+imgname)

main()