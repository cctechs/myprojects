# coding=utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv('creditcard.csv')
# print(data.head())

# 统计label
count_class = pd.value_counts(data['Class'], sort=True).sort_index()
print(count_class)
# count_class.plot(kind='bar') # pandas直接绘图 条形图
#plt.title('Fraud class histogrm')
# plt.xlabel('class')
# plt.ylabel('Frequency')
# plt.show()

# 对amount进行预处理
data['NormAmount'] = StandardScaler().fit_transform(
    data['Amount'].values.reshape(-1, 1))
data = data.drop(['Time', 'Amount'], axis=1)
# print(data.head())

# x and y
X = data.ix[:, data.columns != 'Class']
Y = data.ix[:, data.columns == 'Class']

# number of data
number_records_fraud = len(data[data.Class == 1])
fraud_index = np.array(data[data.Class == 1].index)
# print(fraud_index)
# print(number_records_fraud)

# picking this indices of normal classes
norm_indices = data[data.Class == 0].index
# print(norm_indices)

# 下采样，在class=0的分类中随机选取与class=1相同数量的样本
random_normal_indices = np.random.choice(
    norm_indices, number_records_fraud, replace=False)
random_normal_indices = np.array(random_normal_indices)

# 将数据和样本连接
under_sample_indices = np.concatenate([fraud_index, random_normal_indices])
under_sample_data = data.iloc[under_sample_indices, :]

X_under_sample = under_sample_data.ix[:, under_sample_data.columns != 'Class']
Y_under_sample = under_sample_data.ix[:, under_sample_data.columns == 'Class']

print(len(under_sample_data.ix[data.Class == 0]))

# split all dataset
X_train, X_Test, y_train, y_test = train_test_split(
    X, Y, test_size=0.3, random_state=0)
print('number of train dataset:', len(X_train))
print('number if test dataset:', len(X_Test))

# split undersample dataset
X_under_train, X_under_test, Y_under_train, Y_under_test = train_test_split(X_under_sample, Y_under_sample, test_size=0.3, random_state=0)

print('number of under train dataset:', len(X_under_train)) 
print('number of under test dataset:', len(X_under_test)) 

# recall = tp/(tp +fn)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import confusion_matrix, recall_score, classification_report

#kFold help create cross_validation
def printing_KFold_scores(x_train_data, y_train_data):
    fold = KFold(5, random_state=0, shuffle=False)

    # define L1/L2 parameters
    c_param_range = [0.01, 0.1, 1, 10]

    # save result
    result_table = pd.DataFrame(index=range(len(c_param_range)), columns=['C_parameter', 'Mean_recall_score'])
    result_table['C_parameter'] = c_param_range

    print('x_train_data', type(x_train_data), x_train_data.shape)
    print('y_train_data', type(y_train_data), y_train_data.shape)

    for c_param in c_param_range:
        print('param c:', c_param)
        recall_accs = []
        j = 0
        for train_index, test_index in fold.split(y_train_data):
            lr = LogisticRegression(C=c_param, solver='lbfgs', penalty='l2')

            train_Fetures = x_train_data.iloc[train_index, :]
            train_Label = y_train_data.iloc[train_index, :]

            #print('feautures:', type(train_Fetures), train_Fetures.shape)
            #print('labels:', type(train_Label), train_Label.shape)

            lr.fit(train_Fetures, train_Label.values.ravel())

            # try to test
            X_test_Fetures = x_train_data.iloc[test_index, :]
            y_test_labels = y_train_data.iloc[test_index, :]

            #print('test_fetures:', type(X_test_Fetures), X_test_Fetures.shape)

            y_pred_labels = lr.predict(X_test_Fetures.values)
            #print(y_pred_labels)

            acc = recall_score(y_test_labels, y_pred_labels)
            print('acc:', acc)
            recall_accs.append(acc)
        
        result_table.ix[j, 'mean score'] = np.mean(recall_accs)
        j += 1
        print('mean score', np.mean(recall_accs))
    
import itertools
def plot_confusio_matrix(cm, classes, title='Confusion matric', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def test_confusion_matrix(X_train_data, y_train_data, X_test_data, y_test_data):
    lr = LogisticRegression(C=0.01, penalty='l2', solver='lbfgs')
    lr.fit(X_train_data, y_train_data.values.ravel())
    y_pred = lr.predict(X_test_data.values)

    # compute confusion matrix
    class_names = [0, 1]
    cnf_matrix = confusion_matrix(y_test, y_pred)
    np.set_printoptions(precision=2)
    print(cnf_matrix)
    print('recal matrix:', cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1]))

    plot_confusio_matrix(cnf_matrix, classes=class_names, title='Confusion Matrix')
    plt.show()


test_confusion_matrix(X_under_train, Y_under_train, X_Test, y_test)

#printing_KFold_scores(X_under_train, Y_under_train)