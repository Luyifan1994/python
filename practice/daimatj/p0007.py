# coding: utf-8
# �и�Ŀ¼�����������Լ�д���ĳ���ͳ��һ����д�������д��롣�������к�ע�ͣ�����Ҫ�ֱ��г���
# �����ļ���������py���ļ�
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