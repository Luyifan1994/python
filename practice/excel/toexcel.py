
import xlwt
number = []
name = []

import json  
import xlwt  
from collections import OrderedDict
fname1 = 'student.txt'
fname2 = 'city.txt'
fname3 = 'number.txt'

def student():
	with open(fname1,'r') as f:  
		content = f.read()
	d = json.loads(content,object_pairs_hook=OrderedDict,encoding="gbk")
	print d['1']
	print type(d)
	file = xlwt.Workbook()  
	table = file.add_sheet('test')  
	for row ,i in enumerate(d):
		print row,i
		table.write(row,0,i)    
		for col,j in enumerate(d[i]):  
			table.write(row,col+1,j)  
	file.save('student.xls')
	
def city():
	with open(fname2,'r') as f:  
		content = f.read()
	d = json.loads(content,object_pairs_hook=OrderedDict,encoding="gbk")
	# print d
	file = xlwt.Workbook()
	table = file.add_sheet('test')
	for row,i in enumerate(d):
		table.write(row,0,i)
		table.write(row,1,d[i])
	file.save('city.xls') 
	
def number():
	with open(fname3,'r') as f:  
		content = f.read()
	d = json.loads(content,object_pairs_hook=OrderedDict)
	print type(d)
	file = xlwt.Workbook()
	table = file.add_sheet('test')
	for row,i in enumerate(d):
		for col,j in enumerate(i):
			table.write(row,col,j)
	file.save('number.xls')
	
number()