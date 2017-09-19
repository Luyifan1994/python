# coding: utf-8
# 匹配.c文件中的所有函数名
import re
import glob
import os

class MatchFunc:

    def __init__(self):
        print 'Enter file directory:',
        self.dirc = raw_input()

    def findcfile(self):
        clist = glob.glob(self.dirc + r'\*.c')
        return clist

    def findfunc(self,flist):
        reg = r'(?:status_t|void|bool|uint32_t|int)\s\w+\([^\;]+?\)\n'
        patt = re.compile(reg, re.S)
        os.remove('cfile.txt')
        for c in flist:
            with open(c, 'r') as f:
                data = f.read()
                res = patt.findall(data)
                print c + ' is writing'
                print len(res)
            with open('cfile.txt', 'a') as cf:
                for fc in res:
                    cf.write(fc)
                cf.write('----------------------\n')
        print 'Done'

if __name__ == '__main__':
    match1 = MatchFunc()
    clist1 = match1.findcfile()
    match1.findfunc(clist1)









