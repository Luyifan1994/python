# coding: utf-8
# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
# 遍历文件夹中所有py的文件
import os,linecache
rootdir = r"C:\Work\python"

def getlines(file):
	data = []
	lines = [0,0,0]
	data = linecache.getlines(file)
	for i in range(len(linecache.getlines(file))) : 
		if len(data[i].strip()) == 0:
			lines[0] += 1
		elif data[i].strip()[0] == '#':
			lines[1] += 1
		else:
			lines[2] += 1
		# if data[i] == '\n':
			# eptlines += 1
		# elif (('\t' in data[i]) || (' ' in data[i])):
			# if (data[i].count(' ') + data[i].count('\t') + 1) == length:
				# eptlines += 1
	return lines

def main():
	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			if '.py' in filename:
				# pytext = open(os.path.join(parent,filename),'r')
				lines = getlines(os.path.join(parent,filename))
				print "%s: emptylines-%d, notelines-%d, codelines-%d"%(filename,lines[0],lines[1],lines[2])

main()