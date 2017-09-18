# -*- coding: utf-8 -*-
import linecache,sys

filename = 'log.txt'
data = linecache.getlines(filename)
size = 200
for i in range(len(linecache.getlines(filename))) : 
	if len(data[i]) > size :
		for j in range(len(data[i])):
			sys.stdout.write(data[i][j])
			if ((j+1)%size == 0):
				print('\n')
	else :
		print data[i]