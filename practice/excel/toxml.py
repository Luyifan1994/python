# coding: utf-8
import json
import xlrd
from lxml import etree 
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from collections import OrderedDict
import xml.dom.minidom as minidom
import HTMLParser

fname1 = r'C:\Work\python\excel\student.xls'
xname1 = r'C:\Work\python\excel\student.xml'
node1 = 'student'

fname2 = r'C:\Work\python\excel\city.xls'
xname2 = r'C:\Work\python\excel\city.xml'
node2 = 'city'

fname3 = r'C:\Work\python\excel\number.xls'
xname3 = r'C:\Work\python\excel\number.xml'
node3 = 'number'
comment1 = '''
    <!--
        学生信息表
        "id" : [名字, 数学, 语文, 英文]
    -->
'''
comment2 = '''
     <!-- 
        城市信息
     -->
'''
comment3 = '''
     <!-- 
        数字信息
     -->
'''
def xlstostr(fname):
	data = xlrd.open_workbook(fname)
	table = data.sheets()[0]
	str = ""
	d = OrderedDict()
	e = []
	for i in range(table.nrows):
		value = table.row_values(i)
		if 'student' in fname:
			d[value[0]]= value[1:]
			str = json.dumps(d,indent = 4,ensure_ascii=False,encoding="utf-8")
		elif 'city' in fname:
			d[value[0]]= value[1]
			str = json.dumps(d,indent = 4,ensure_ascii=False,encoding="utf-8")
		else:
			e.append(value)
			str = json.dumps(e,indent = 4,ensure_ascii=False,encoding="utf-8")
		# str += (json.dumps(d,ensure_ascii=False,encoding="utf-8")+"\n")
	# return str[:-1]
	return str

# def xlstostr2(fname):
	# data = xlrd.open_workbook(fname)
	# table = data.sheets()[0]
	# str = ""
	# d = OrderedDict()
	# for i in range(table.nrows):
		# value = table.row_values(i)
		# d[value[0]]= value[1]
	# str = json.dumps(d,indent = 4,ensure_ascii=False,encoding="utf-8")
	# return str

# def modify(fileName):
	# doc = etree.parse(fileName)
	# root = doc.getroot()
	# for child in list(root):
		# child.tail = "\n"
	# doc.write(fileName,encoding='utf-8')

def modify(filename):
	file = open(filename,'r')
	cont = file.read()
	html_parser = HTMLParser.HTMLParser()
	tranform = html_parser.unescape(cont)
	file_trans = open(filename,'w')
	file_trans.write(tranform)

class makexml():
	def __init__(self, xmlpath):
		self.xmlpath = xmlpath
		self.dom = minidom.DOMImplementation().createDocument(None, 'root', None)
		self.root = self.dom.documentElement

	def creat_node(self, node_name, node_text=None, comment=None):
		if None == node_text:
			newnode = self.dom.createElement(node_name)
		else:
			if None != comment:
				newtext = self.dom.createTextNode(comment+node_text)
			else:
				newtext = self.dom.createTextNode(node_text)
			newnode = self.dom.createElement(node_name)
			newnode.appendChild(newtext)
		return newnode

	def add_child(self, item, node,comment=None):
		new_node = self.creat_node(node,item,comment)
		self.root.appendChild(new_node)
	
	def save(self):
		with open(self.xmlpath, 'w') as f:
			self.dom.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
			# html_parser = HTMLParser.HTMLParser()  
			# tranform = html_parser.unescape(self.dom.toxml().decode('utf-8')) #转换转译字符
			# f.write(tranform.encode('utf-8'))


	
def main(fname,xname,comment,node):
    newxml = makexml(xname)
    newxml.add_child(xlstostr(fname),node,comment)
    newxml.save()
    modify(xname)

if __name__ =="__main__":
	main(fname1,xname1,comment1,node1)
	main(fname2,xname2,comment2,node2)
	main(fname3,xname3,comment3,node3)