#coding=utf-8

import numpy as np

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

    

if __name__ == '__main__':
    pass