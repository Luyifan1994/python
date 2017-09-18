# -*- coding: utf-8 -*-
import xlrd
from lxml import etree
import codecs
from collections import OrderedDict
import sys
reload(sys)
sys.setdefaultencoding('utf8')

path = "C:\Work\python\excel/student.xls"
attr = ["ID", "Name", "Chinese", "Math", "English"]
comment = '''
    <!--
        学生信息表
        "id" : [名字, 数学, 语文, 英文]
    -->
'''

def xlstojson(path):
	data = xlrd.open_workbook(path)
	table = data.sheets()[0]
	for i in range(table.nrows):
		d = OrderedDict()
		value = table.row_values(i)
		d[value[0]]= value[1:]


def xls_to_xml(path):
	root = etree.Element("root")
	root.tail = "\n"
	student_xml = etree.ElementTree(root)
	sub = etree.SubElement(student_xml.getroot(), "student")
	sub.tail = "\n"
	data = xlrd.open_workbook(path)
	table = data.sheets()[0]
	for i in range(table.nrows):
		d = OrderedDict()
		value = table.row_values(i)
		d[value[0]]= value[1:]
		sub.text = json.dumps(d)+"\n"


    output = codecs.open("student2.xml", "w")
    output.write(etree.tounicode(student_xml.getroot()))
    output.close()


if __name__ == "__main__":
    xls_to_xml(path)