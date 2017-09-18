# coding: utf-8
# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights
import linecache

filename = 'filtered_words.txt'
file = open(filename,'r')
line = file.readlines()
data = []

def change1():
	for i in range(len(line)):
		data.append(line[i].strip())
	print 'input words:'
	input = raw_input()
	print input
	print data
	if input in data :
		print 'Freedom'
	else:
		print 'Human Rights'

def change2():
	output = []
	print 'input words:'
	input = raw_input()
	for i in range(len(line)):
		data.append(line[i].strip())
		if data[i] in input:
			if len(output) == 0:
				output.append(input.replace(data[i],len(data[i])*'*'))
			else:
				output[0] = (output[0].replace(data[i],len(data[i])*'*'))
	print 'new output:\n' + output[0]

change2()