# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import operator
# 将文本记录进行转换
def file2matrix(filename):
    fr = open(filename)
    lines = len(fr.readlines())
    print ('lines:', lines)

    # 生成空矩阵
    returnMatrix = np.zeros((lines, 3))
    lables = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMatrix[index,:] = listFromLine[0:3]
        lables.append(int(listFromLine[-1]))
        index += 1
    return returnMatrix, lables

# 数据归一化
# 将需要处理的数据经过处理后限制在一定的范围内
# 归一化在0-1之间的作用是统计概率分布，归一化在[-1,1]之间是统计坐标分布
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    rangeValue = maxVals - minVals
    normData = np.zeros(np.shape(dataSet))
    m = normData.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet/np.tile(rangeValue, (m ,1))
    return normData, rangeValue, minVals

# 训练算法, KNN算法不需要
def train():
    pass

# 分类
def classify(X, dataset, labels, k):
    nSize = dataset.shape[0]
    diffMat = np.tile(X, (nSize, 1)) - dataset
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance**0.5

    # 按距离排序, 返回值是索引的序列
    sortedDistIndices = distance.argsort()
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDistIndices[i]]
        classCount[votelabel] = classCount.get(votelabel,0)+1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1))
    return sortedClassCount[0][0]

# 测试
def Test():
    ratio = 0.1
    data, labels = file2matrix('datingTestSet2.txt')
    normData, ranges, minvals = autoNorm(data)
    m = data.shape[0]
    nTestNum = int(m*ratio)
    print 'testNum:', nTestNum
    errCount = 0.0
    for i in range(nTestNum):
        result = classify(normData[i,:],normData[nTestNum:m, :], labels[nTestNum:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (result, labels[i])
        if (result != labels[i]): 
            errCount += 1.0
    print "the total error rate is: %f" % (errCount / float(nTestNum))
    print errCount


def plot_data(data, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.scatter(data[:, 0], data[:,1], 15.0*np.array(labels), 15.0*np.array(labels))
    ax.scatter(data[:, 0], data[:,1], c=np.array(labels))
    plt.show()

if __name__ == '__main__':
    Test()
     

