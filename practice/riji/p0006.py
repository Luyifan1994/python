# -*- coding: utf-8 -*-
# ����һ��Ŀ¼��������һ���µ��ռǣ����� txt��Ϊ�˱���ִʵ����⣬�������ݶ���Ӣ�ģ���ͳ�Ƴ�����Ϊÿƪ�ռ�����Ҫ�Ĵʡ�
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