import os,glob
import sys

search_path = r'C:\Work\mcu-sdk-2.0\devices'
print 'Enter what you want to search:'
search_unit = raw_input()

def gethfile(path):
	hfile = []
	for f in glob.glob(path+r'\*\*.h'):
		name1 = f.split('\\')[4]
		name2 = f.split('\\')[-1].split('.')[0]
		if (name2 == name1) |  (name2 == (name1 + '_cm4')):
			hfile.append(f)
	return hfile
	
def search(hfile,unit):
	result = []
	for hf in hfile:
		fp = open(hf,'r')
		data = fp.read()
		if unit in data:
			print hf + 'is done'
			result.append(hf)
		else:
			print hf + ' is done'
		fp.close()
	return result

if __name__ == '__main__':
#	log_file = sys.stdout
#	f = open('log.txt','w')
#	sys.stdout = f
	
	print '**********' + '[ ' + search_unit + ' ]' + ' Search' + '**********'
	hfile = gethfile(search_path)
	res = search(hfile,search_unit)
	print '\n',
	print 'The search result is'
	if len(res) == 0:
		print 'None!'
	for r in res:
		print r
#	sys.stdout = log_file
#	f.close()
#	print 'The search is done.To see more in log.txt'