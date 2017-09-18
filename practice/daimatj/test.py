
name = r'C:\Work\python\daimatj\aaa.txt'
file = open(name,'r')
data = file.readlines()
print data[0].strip()[0]
# print (data[1].count(' ') + data[1].count('\t') + 1) == len(data[1])