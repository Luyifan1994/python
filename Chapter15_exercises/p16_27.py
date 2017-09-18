from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime
import re

class RandData:
    def __init__(self):
        self.domain = ['com', 'edu', 'net', 'org', 'gov']
        self.fname = r'redata.txt'

    def getdata(self):
        f = open(self.fname, 'w')
        st = ''
        for i in range(randint(5, 10)):
            dtint = randint(0, maxint - 1)
            dtstr = ctime(dtint)

            shorter = randint(4, 7)
            em = ''
            for j in range(shorter):
                em += choice(lowercase)

            longer = randint(shorter, 12)
            dn = ''
            for j in range(longer):
                dn += choice(lowercase)

            st += '%s::%s@%s.%s::%d-%d-%d\n' % (dtstr, em,
                                            dn, choice(self.domain), dtint, shorter, longer)
        f.write(st)
        f.close()

    def weektimes(self):
        week = []
        with open(self.fname, 'r') as f:
            for lines in f.readlines():
                patt = r'^\w{3}'
                reg = re.compile(patt)
                result = reg.search(lines)
                if result is not None:
                    week.append(result.group())
                else:
                    print 'line %d has no week name' % f.readlines().index(lines)
        mon = week.count('Mon')
        tue = week.count('Tue')
        wed = week.count('Wed')
        thu = week.count('Thu')
        fri = week.count('Fri')
        sat = week.count('Sat')
        sun = week.count('Sun')
        print 'Matching: Mon-%d, Tue-%d, Wed-%d, Thu-%d, Fri-%d, Sat-%d, Sun-%d' % (mon, tue, wed, thu, fri, sat, sun)

    def timematch(self):
        match = 0
        with open(self.fname, 'r') as f:
            data = f.readlines()
            for lines in data:
                patt1 = r'^(.+)::[a-z]'
                patt2 = r'::(\d+)-'
                reg1 = re.compile(patt1)
                reg2 = re.compile(patt2)
                time = reg1.search(lines)
                strnum = reg2.search(lines)
                if (time is not None) & (strnum is not None):
                    # print time.group(1)
                    # print ctime(int(strnum.group(1)))
                    if time.group(1) == ctime(int(strnum.group(1))):
                        match += 1
                else:
                    print 'Match Error'
            # print match
            # print len(data)
            if match == len(data):
                print 'All data about time is matched well'

    def regmatch(self):
        with open(self.fname, 'r') as f:
            patt = [r'^(.+)::[a-z]', r'::(.+)::', r'\s([A-Za-z]{3})\s',
                    r'\s(\d+)::', r'\s(\d+:\d+:\d+)\s', r'::(\w+)@(.+)::']
            i = 0
            for lines in f.readlines():
                i += 1
                match = []
                for p in patt:
                    reg = re.compile(p)
                    res = reg.search(lines)
                    if res is not None:
                        if patt.index(p) != (len(patt) - 1):
                            match.append(res.group(1))
                        else:
                            match.append(str(res.groups()))
                    else:
                        match.append('none')
                # print 'line: %s\n' % str(match)
                print 'Line%d: %s' % (i, str(match))

    def updatemail(self,email):
        patt = r'[a-z]+@[a-z\.]+'
        with open(self.fname,'r') as f:
            for i,line in enumerate(f):
                print 'line' + str(i+1) + ':',
                print re.sub(patt,email,line),

    def outtime(self):
        patt = r'\s(\w+\s\w+).+\s(\d+)::'
        reg = re.compile(patt)
        with open(self.fname,'r') as f:
            for i,line in enumerate(f):
                res = reg.search(line)
                if res is not None:
                    print 'line %d: %s, %s' % (i+1, res.group(1),res.group(2))
                else:
                    print 'line %d : unmatch' % (i+1)


if __name__ == '__main__':
    ob = RandData()
    ob.getdata()
    # ob.weektimes()
    # ob.timematch()
    # ob.regmatch()
    # ob.updatemail('1234@qq.com')
    # ob.outtime()
