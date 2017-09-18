# -*- coding: utf-8 -*-
# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import glob
rootdic = r"C:\Work\python\riji"

def findchar(fname,wd):
	file = open(fname,'r')
	data = file.readlines()
	num = 0
	for i in range(len(data)):
		num += data[i].count(wd)
	return num

def main():
	word = raw_input('input words: ')
	total = 0
	for filename in glob.glob(rootdic+r"\*.txt"):
		charnum = 0
		txtname = filename.split("\\")[-1]
		charnum = findchar(filename,word)
		total += charnum
		print "%s - %s : %d"%(txtname,word,charnum)
	print "total words: %d"%total
	

main()