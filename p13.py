import re

obj = dir
out = type(obj)
patt = r'\'(.+)\''
reg = re.compile(patt)
res = reg.search(str(out))
if res is not None:
    print res.group(1)
else:
    print 'unmatched type'