import re

patt = r'^((0|[1-9]\d*)\.?\d*)\+?((0|[1-9]\d*)\.?\d*)[ij]$'
str1 = raw_input()
reg = re.compile(patt)
res = reg.search(str1)
if res is not None:
    print res.group()
else:
    print 'unmatch'


