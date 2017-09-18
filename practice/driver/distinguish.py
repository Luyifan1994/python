# coding: utf-8
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import os,glob

ktsRMdic = r'C:\Work\driver\kenetis_RM2'
lpcRMdic = r'C:\Work\driver\lpc_RM'
pkgktsdir1 = r'C:\Release\REL6\windows\kenetis'
pkgktsdir2 = r'C:\Release\REL5\REL5_RC3\windows'
pkglpcdir = r'C:\Release\REL6\windows\lpc'
sdkdir = r'C:\Work\mcu-sdk-2.0\boards'
drvdir = r'C:\Work\driver\drivers'
ktsdir = r'C:\Work\driver\kenetis'
lpcdir = r'C:\Work\driver\lpc'
matchdir = r'C:\Work\driver\match.txt'
unmatchdir = r'C:\Work\driver\unmatch.txt'
matchdrv = {}
unmatchdrv = {}

def getICdrivers(filename):
	# 打开一个pdf文件
	ICdriver = []
	fp = open(filename, 'rb')
	# 获得文档的目录（纲要）
	parser = PDFParser(fp)
	document = PDFDocument(parser)
	outlines = document.get_outlines()
	# 获取芯片driver的名字
	for (level,title,dest,a,se) in outlines:
		if (level == 1) & ('(' in title):
			ICdriver.append(title.split('(')[-1].split(')')[0].lower())
	fp.close()
	return ICdriver

def getdrivers(driverdirc):
	for parent,dirnames,filenames in os.walk(driverdirc):
		return dirnames
		break

def getname(RMpath):
	if 'lpc' in RMpath:
		return glob.glob(RMpath + r'\*.pdf')
	else:
		return glob.glob(RMpath + r'\*\*.pdf')

def match(icdriver,alldriver,ICname):
	global matchdrv
	global unmatchdrv
	matchname = []
	unmatchname = icdriver
	for adriver in alldriver:
		for idriver in icdriver:
			if (idriver == adriver):
				matchname.append(idriver)
	matchdrv[ICname] = matchname
	for name in matchname:
		unmatchname.remove(name)
	unmatchdrv[ICname] = unmatchname

def getdvrfrompkg(path):
	pkgdriver = {}
	for drvpath in glob.glob(path+r'\*\*\*\driver_examples'):
		name = drvpath.split('\\')[-2]
		for parent,dirnames,filenames in os.walk(drvpath):
			if parent == drvpath:
				pkgdriver[name] = dirnames
	return pkgdriver

def getdrvfromsdk(path,kind):
	sdkdriver = {}
	if kind == 'kenetis':
		for drvpath in glob.glob(path+r'\*\driver_examples'):
			name = drvpath.split('\\')[-2]
			if (name.find('frdm') == 0) | (name.find('twr') == 0) | (name.find('usb') == 0):
				for parent,dirnames,filenames in os.walk(drvpath):
					if parent == drvpath:
						sdkdriver[name] = dirnames
	elif kind == 'lpc':
		for drvpath in glob.glob(path+r'\*\driver_examples'):
			name = drvpath.split('\\')[-2]
			if (name.find('lpc') == 0):
				for parent,dirnames,filenames in os.walk(drvpath):
					if parent == drvpath:
						sdkdriver[name] = dirnames
	return sdkdriver

def merge(dic):
	mergelist = []
	for k in dic.keys():
		mergelist = list(set(mergelist+dic[k]))
	return mergelist

def cutandpaste(source,destination,matchname):
	for name in matchname:
		srcpath = os.path.join(source,name)
		src2path = os.path.join(srcpath,'doxygen')
		dstpath = os.path.join(destination,name)
		dst2path = os.path.join(dstpath,'doxygen')
		md1_cmd = r'md "%s"'%dstpath
		md2_cmd = r'md "%s"'%dst2path
		copy1_cmd = r'copy /Y "%s" "%s"'%(srcpath,dstpath)
		copy2_cmd = r'copy /Y "%s" "%s"'%(src2path,dst2path)
		del1_cmd = r'del /S /Q %s'%srcpath
		del2_cmd = r'rd /S /Q %s'%srcpath
		os.system(md1_cmd)
		os.system(md2_cmd)
		os.system(copy1_cmd)
		os.system(copy2_cmd)
		os.system(del1_cmd)
		os.system(del2_cmd)

def write_txt(dic,fname):
	file = open(fname,'a+')
	for k in dic.keys():
		wirte_str = str(k) + ':' + str(dic[k]) + '\n'
		file.write(wirte_str)
	file.close()

def rm_main(rmdir,cutdir):
	global matchdrv
	global unmatchdrv
	RMpath = getname(rmdir)
	# print RMpath
	for fname in RMpath:
		icname = fname.split('\\')[-1].split('.')[0]
		# print icname
		icdrv = getICdrivers(fname)
		# print icdrv
		alldrv = getdrivers(drvdir)
		match(icdrv,alldrv,icname)
		# print matchdrv
		matchlist = merge(matchdrv)
		# print matchlist
		# print len(matchlist)
		# print matchdrv
	write_txt(matchdrv,matchdir)
	write_txt(unmatchdrv,unmatchdir)
	cutandpaste(drvdir,cutdir,matchlist)
	print matchlist
	print len(matchlist)

def pkg_main(pkgdir,cutdir):
	global matchdrv
	global unmatchdrv
	pkgdrv = getdvrfrompkg(pkgdir)
	alldrv = getdrivers(drvdir)
	for k in pkgdrv.keys():
		match(pkgdrv[k],alldrv,k)
		matchlist = merge(matchdrv)
	write_txt(matchdrv,matchdir)
	write_txt(unmatchdrv,unmatchdir)
	cutandpaste(drvdir,cutdir,matchlist)
	print matchlist
	print len(matchlist)

def sdk_main(sdkpath,cutdir):
	global matchdrv
	global unmatchdrv
	if 'kenetis' in cutdir:
		kind = 'kenetis'
	elif 'lpc' in cutdir:
		kind = 'lpc'
	sdkdrv = getdrvfromsdk(sdkpath,kind)
	alldrv = getdrivers(drvdir)
	for k in sdkdrv.keys():
		match(sdkdrv[k],alldrv,k)
		matchlist = merge(matchdrv)
	write_txt(matchdrv,matchdir)
	write_txt(unmatchdrv,unmatchdir)
	cutandpaste(drvdir,cutdir,matchlist)
	print matchlist
	print len(matchlist)

#rm_main(ktsRMdic,ktsdir)
#pkg_main(pkgktsdir1,ktsdir)
#pkg_main(pkgktsdir2,ktsdir)
#sdk_main(sdkdir,ktsdir)
#rm_main(lpcRMdic,lpcdir)
#pkg_main(pkglpcdir,lpcdir)
sdk_main(sdkdir,lpcdir)