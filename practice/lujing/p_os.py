# coding: utf-8
# 小程序：根据用户输入选择可以完成以下功能：
# 创建文件，如果路径不存在，创建文件夹后再创建文件
# 能够查看当前路径
# 在当前目录及其所有子目录下查找文件名包含指定字符串的文件

import os

class FuncFile:

    def __init__(self):
        self.dirname = os.getcwd()

    def createfile(self, dname,fname):
        filename = os.path.join(dname,fname)
        if os.path.exists(dname) is False:
            os.mkdir(dname)
            open(filename,'w').close()
            print("%s目录已创建完成,%s文件已创建完成" % (dname, fname))
        elif os.path.exists(filename) is False:
            open(filename,'w').close()
            print("%s文件已创建完成" % filename)
        else:
            print '%s文件已经存在'

    def getdir(self):
        print '当前路径为%s' % self.dirname

    def getfile(self,patt):
        match = 0
        for i in os.walk(self.dirname):
            for j in i[-1]:
                if j.find(patt) > -1 :
                    match += 1
                    print (os.path.join(i[0],j))
            if match == 0:
                print 'unmatch'


if __name__ == '__main__':
    print '''1 - 创建文件
2 - 获取当前路径
3 - 查找文件'''

    func = FuncFile()
    cmd = raw_input()

    if cmd == '1':
        print '输入路径名：',
        dn = raw_input()
        print '输入文件名：',
        fn = raw_input()
        func.createfile(dn,fn)
    elif cmd == '2':
        func.getdir()
    else:
        print '输入文件所包含的字符串：',
        pat = raw_input()
        func.getfile(pat)
