import os,glob
import re
import xlwt,xlrd
from xlutils.copy import copy

ktspath = r'C:\Work\driver\kenetis'
lpcpath = r'C:\Work\driver\lpc'
testpath = r'C:\Work\driver\test'
excelname = r'C:\Work\driver\driver.xls'

def set_font(font_name,font_bold,font_color,font_height):
	font = xlwt.Font()
	font.name = 'Arial'
	font.bold = font_bold
	font.color_index = font_color
	font.height = font_height
	return font

def set_border(border_width):
	borders= xlwt.Borders()
	borders.left= border_width
	borders.right= border_width
	borders.top= border_width
	borders.bottom= border_width
	return borders

def set_pattern(pattern_color):
	pattern = xlwt.Pattern()
	pattern.pattern = xlwt.Pattern.SOLID_PATTERN
	pattern.pattern_fore_colour = pattern_color # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
	return pattern

def set_alignment(horz,verz):
	alignment = xlwt.Alignment() # Create Alignment
	if horz == 1:
		alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL,HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED,HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
	if verz == 1:
		alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP,VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
	return alignment

def set_style(blod,height,color,hz,vz):
	style = xlwt.XFStyle()
	style.font = set_font('Arial',blod,1,height)
	style.borders = set_border(1)
	style.pattern = set_pattern(color)
	style.alignment = set_alignment(hz,vz)
	return style

def get_driver(path):
	str = ''
	if 'kenetis' in path:
		for parent,dirnames,filenames in os.walk(path):
			if parent == path:
				for i in range(len(dirnames)):
					if i != (len(dirnames) - 1):
						dirnames[i] += '\n'
						str += dirnames[i]
					else:
						str += dirnames[i]
		return str
	else:
		for parent,dirnames,filenames in os.walk(path):
			if parent == path:
				return dirnames

def init_excel(fname):
	row_title = ['Drivers','Cfile','APIs','Call APIs?']
	col_title = ['Kenetis','LPC']
	
	file = xlwt.Workbook()
	sheet = file.add_sheet('driver',cell_overwrite_ok = True)
	
	for i in range(0,len(row_title)):
		sheet.write(1,(i+2),row_title[i],set_style(True,220,1,1,1))
	
	for j in range(0,len(col_title)):
		sheet.write((j+2),1,col_title[j],set_style(True,220,1,1,1))
	
	file.save(fname)

def write_driver(driver_path,fname):
	driver = get_driver(driver_path)
	
	rb = xlrd.open_workbook(fname,formatting_info=True)
	wb = copy(rb)
	sheet = wb.get_sheet(0)
	
	if 'lpc' in driver_path:
#		sheet.write_merge(3,(2+len(driver)),1,1,'LPC',set_style(True,220,5,True))
		for k in range(0,len(driver)):
			sheet.write((k+3),2,driver[k],set_style(False,200,1,1,1))
	else:
			sheet.write(2,2,driver,set_style(False,200,1,1,1))
	
	os.remove(fname)
	wb.save(fname)
	
def write_api(driver_path,fname):
	apis = getCfile(driver_path)
	j = 0
	h = 0
	rb = xlrd.open_workbook(fname,formatting_info=True)
	wb = copy(rb)
	sheet = wb.get_sheet(0)
	
	for k,v in apis.items():
		p = 0
		for m,n in v.items():
			for i in range(len(n)):
				if 'base' in n[i]:
					sheet.write((i+j+3),5,'No',set_style(False,180,1,1,1))
				sheet.write((i+j+3),4,n[i],set_style(False,180,1,0,1))
			sheet.write_merge(j+3,(j+len(n)+2),3,3,m,set_style(False,200,1,1,1))
			j+=len(n)
#			print 'j:' + str(j)
			p+=len(n)
#			print 'p:' + str(p)
		sheet.write_merge(h+3,(h+p+2),2,2,k,set_style(False,200,1,1,1))
		h += p
#		print 'h:' + str(h)
#		print '\n',
	sheet.write_merge(3,(2+j),1,1,'LPC',set_style(True,220,1,1,1))
	
	os.remove(fname)
	wb.save(fname)

	
def getCfile(path):
	func = {}
	for folder in glob.glob(path + r'\*'):
		dvname = folder.split('\\')[-1]
		func[dvname] = {}
	
	for cfile in glob.glob(path + r'\*\*.c'):
		funclist = []
#		print cfile
		name1 = cfile.split('\\')[-2]
		name2 = cfile.split('\\')[-1].split('.')[0]
#		print name2
#		cname = name1 + r'_' + name2
		file = open(cfile,'r')
		data = file.read()
#		print data
		# void,status_t,bool,uint32_t
		reg = r'status_t\s\w+?\({1}?.+?\){1}?|void\s\w+?\({1}?.+?[^\;]\){1}?|bool\s\w+?\({1}?.+?\){1}?|uint32_t\s\w+?\({1}?.+?\){1}?|int\s\w+?\({1}?.+?\){1}?'
# 
#		print reg
		funcre = re.compile(reg,re.S)
		list1 = funcre.findall(data)
		list2 = []
		for str1 in list1:
			if str1 not in list2:
				list2.append(str1)
		for str2 in list2:
			funclist.append(str2.replace('  ','').replace('\n',''))
#		print len(list)
#		print funclist
#		print len(funclist)
		if len(funclist) == 0:
			funclist.append('None')
		
		func[name1][name2] = funclist
		file.close()
	
	for k in func.keys():
		if len(func[k]) == 0:
			func[k]['None'] = ['None']
	
	return func

if __name__ == '__main__':
#	a = getCfile(lpcpath)
#	for k,v in a.items():
#		print k + ':'
#		for m,n in v.items():
#			print m + ':' + str(n)
#			print m + ':' + str(len(n))
#		print '\n',
	init_excel(excelname)
	write_driver(ktspath,excelname)
	write_api(lpcpath,excelname)