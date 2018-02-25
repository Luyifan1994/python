# coding: utf-8
# k-近邻算法

from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.1], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classfiy0(intx, dataset, labels, k):
    datasetsize = dataset.shape[0]
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
    print classcount
    sortdclasscount = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
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


if __name__ == '__main__':
    # 测试file2matrix的近邻算法
    # a, b = createDataSet()
    # result = classfiy0([0.8, 0.7], a, b, 3)
    # print result
    # 测试matplotlib的散点图
    datapth = r'machinelearninginaction\Ch02\datingTestSet2.txt'
    datamat, labels = file2matrix(datapth)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(datamat[:, 1], datamat[:, 2], 15 * array(labels), 15 * array(labels))
    plt.show()
