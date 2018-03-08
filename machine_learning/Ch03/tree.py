# coding:utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from math import log
import operator


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    # change to discrete values
    return dataSet, labels


# 计算香农熵
def calcShannonEnt(dataset):
    numEntries = len(dataset)
    labelcounts = {}
    for featvec in dataset:
        currentlabel = featvec[0]
        if currentlabel not in labelcounts.keys():
            labelcounts[currentlabel] = 0
        labelcounts[currentlabel] += 1
    shannonEnt = 0.0
    # print labelcounts
    for key in labelcounts:
        prob = float(labelcounts[key]) / float(numEntries)
        # print prob
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# 划分数据集
def splitDataset(dataset, axis, value):
    retdataset = []
    for featvec in dataset:
        if featvec[axis] == value:
            reducedfeatvec = featvec[:axis]
            reducedfeatvec.extend(featvec[axis + 1:])
            retdataset.append(reducedfeatvec)
    return retdataset


# 选择最好的数据集划分方式
def chooseBestFeature(dataset):
    numFeatures = len(dataset[0]) - 1
    baseEntropy = calcShannonEnt(dataset)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featlist = [example[i] for example in dataset]
        # print featlist
        uniqueVals = set(featlist)  # 去重
        # print uniqueVals
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataset(dataset, i, value)
            prob = len(subDataSet) / float(len(dataset))
            newEntropy += prob * calcShannonEnt(subDataSet)  # 划分数据集信息熵的数学期望
            # print calcShannonEnt(subDataSet)
        # print i
        # print newEntropy
        infogain = baseEntropy - newEntropy
        if infogain > bestInfoGain:
            bestInfoGain = infogain
            bestFeature = i
    return bestFeature


def majorityCnt(classlist):
    classcount = {}
    for vot in classlist:
        if vot not in classcount.keys():
            classcount[vot] = 0
        classcount += 1
    sortedclasscount = sorted(classcount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedclasscount[0][0]


def createTree(dataset, labels):
    classlist = [example[-1] for example in dataset]
    if classlist.count(classlist[0]) == len(classlist):
        return classlist[0]
    if len(dataset[0]) == 1:
        return majorityCnt(classlist)
    bestFeat = chooseBestFeature(dataset)
    bestFeatLabel = labels[bestFeat]
    mytree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataset]
    uniquevals = set(featValues)
    for value in uniquevals:
        sublabels = labels[:]
        mytree[bestFeatLabel][value] = createTree(splitDataset(dataset, bestFeat, value), sublabels)

    return mytree


if __name__ == '__main__':
    # 测试计算信息增量
    dataset, labels = createDataSet()
    # print calcShannonEnt(dataset)

    # 选择最好的数据集划分方式
    # print chooseBestFeature(dataset)

    # 创建决策树
    print createTree(dataset, labels)
