
def cttext():
	n = raw_input('input a character: ')
	fname = 'abc.txt'
	file = open(fname,'r')
	data = []
	data = file.readlines()
	num = 0
# print len(data)
	for i in range(len(data)):
		num += data[i].count(n)
	print (("The number of %s is %d")%(n,num))

cttext()