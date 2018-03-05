# coding: utf-8
# k-近邻算法

from numpy import *
import operator
# import matplotlib
import matplotlib.pyplot as plt

datapath = 'machinelearninginaction/Ch02/datingTestSet2.txt'


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.1], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classfiy0(intx, dataset, labels, k):
    datasetsize = dataset.shape[0]
    # print intx
    # print datasetsize
    # print shape(dataset)
    diffmat = tile(intx, (datasetsize, 1)) - dataset  # 复制一个与dataset相同的array,与dataset作差
    # print diffmat
    sqdiffmat = diffmat ** 2
    sqdistance = sqdiffmat.sum(axis=1)
    distance = sqdistance ** 0.5  # 计算欧式距离
    # print distance
    sortdistance = distance.argsort()
    classcount = {}
    for i in range(k):  # 选择距离最小的k个点，取次数最多的点的标签作为结果
        votelabel = labels[sortdistance[i]]
        classcount[votelabel] = classcount.get(votelabel, 0) + 1
    # print classcount
    sortdclasscount = sorted(classcount.items(), key=operator.itemgetter(1),
                             reverse=True)  # operator.itemgetter(1)按照第二列的值排序
    return sortdclasscount[0][0]


def file2matrix(filename):
    with open(filename, 'r') as f:
        arraylines = f.readlines()
    numberlines = len(arraylines)
    returnmat = zeros((numberlines, 3))
    classlabels = []
    for index, line in enumerate(arraylines):
        line = line.strip()
        listline = line.split('\t')
        returnmat[index, :] = listline[0:3]
        classlabels.append(int(listline[-1]))
    return returnmat, classlabels


def autoNorm(dataset):
    minvals = dataset.min(0)  # 参数0表示按列取最小值
    maxvals = dataset.max(0)
    # print minvals
    ranges = maxvals - minvals
    # print ranges
    normdateset = zeros(shape(dataset))  # 防止变量不存在
    m = dataset.shape[0]
    normdateset = dataset - tile(minvals, (m, 1))
    # print normdateset
    # print tile(minvals, (m, 1))
    normdateset = normdateset / tile(ranges, (m, 1))
    return normdateset, ranges, minvals


def datingclasstest():
    hoRatio = 0.10
    datingDateMat, datingLables = file2matrix(datapath)
    normMat, ranges, minvals = autoNorm(datingDateMat)
    m = normMat.shape[0]
    numtestvecs = int(m * hoRatio)
    errorcount = 0.0
    for i in range(numtestvecs):
        classifierResult = classfiy0(normMat[i,:], normMat[numtestvecs:m, :], datingLables[numtestvecs:m], 3)
        print "test_result:%d, real_answer:%d" % (classifierResult, datingLables[i])
        if classifierResult != datingLables[i]:
            errorcount += 1.0
    print "error rate:%f" % (errorcount / float(numtestvecs))


if __name__ == '__main__':
    # 测试近邻算法
    # a, b = createDataSet()
    # result = classfiy0([0.8, 0.7], a, b, 3)
    # print result

    # 测试matplotlib的散点图
    # datamat, labels = file2matrix(datapath)
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.scatter(datamat[:, 1], datamat[:, 2], s=15 * array(labels), c=15 * array(labels)) #scatter表示散点图, s表示大小，c表示颜色
    # plt.show()

    # 测试归一化数值autoNorm
    # datamat, labels = file2matrix(datapath)
    # normmat, ranges, minvals = autoNorm(datamat)
    # print normmat

    # 测试分类器
    # datingclasstest()
