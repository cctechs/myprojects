#coding=utf-8

import numpy as np
from math import log

# 构造数据
def createDataSet():
    dataSet = [[1,1,'yes'],
    [1,1,'yes'],
    [1,0,'no'],
    [0,1,'no'],
    [0,1,'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

# 计算香农熵的函数
def calShannonEnt(dataSet):
    nNum = len(dataSet)
    labelCount = {}
    for feature in dataSet:
        #print type(feature)
        currentLabel = feature[-1]
        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1
        print 'feature, count', currentLabel, labelCount[currentLabel]

    shannonEnt = 0.0
    for key in labelCount: 
        prob = float(labelCount[key])/nNum
        shannonEnt -= prob*log(prob, 2)
    return shannonEnt

def splitDataSet(dataSet, index, value):
    

if __name__ == '__main__':
    dataSet, labels = createDataSet()
    r = calShannonEnt(dataSet)
    print r