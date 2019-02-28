# coding=utf-8

# cross_val_score 交叉验证用于参数选择，模型选择，特征选择

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import pandas as pd
from sklearn.model_selection import cross_validate, KFold
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris()
X = iris.data
y = iris.target

print('X:', len(X), type(X))
print('y:', len(y), type(y))

for i in range(1, 5):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i)
    knn = KNeighborsClassifier(n_neighbors=5)

    #print(len(X_train), type(X_train))
    #print(len(y_train), type(y_train))
    # break
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(metrics.accuracy_score(y_test, y_pred))


kf = KFold(n_splits=5, shuffle=False)

X_train = pd.DataFrame(X)
y_train = pd.DataFrame(y)


knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
print('scores:', scores)
print('scores mean:', scores.mean())


for train_index, test_index in kf.split(X_train):
    x_tr = X_train.iloc[train_index, :]
    y_tr = y_train.iloc[train_index, :]
    # print(x_tr)
    # print(y_tr)


from sklearn import metrics
print('\n help to choose features')
data = pd.read_csv(
    'http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
print(data.head())

###
features_cols = ['TV', 'radio', 'newspaper']
X = data[features_cols]
y = data['sales']
print(sorted(metrics.SCORERS.keys()))
lr = LinearRegression()
scores = cross_val_score(lr, X, y, cv=10, scoring='neg_mean_squared_error')
print('liner scores111:', scores.mean())
import numpy as np
v = np.sqrt(-scores)
print('rmse111:', v.mean())


features_cols = ['TV', 'radio']
X = data[features_cols]
y = data['sales']
lr = LinearRegression()
scores = cross_val_score(lr, X, y, cv=10, scoring='neg_mean_squared_error')
print('liner scores222:', scores.mean())
import numpy as np
v = np.sqrt(-scores)
print('rmse222:', v.mean())
