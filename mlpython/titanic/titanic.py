# conding=utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('titanic_train.csv')

# count missing data
num = data.count()

# plot data
#columns = data.columns
#plt.bar(columns, num)
#plt.xticks(rotation=30)
#plt.show()

print(data.count())

# fill age
mean_age = data['Age'].median()
print('mean_age:', mean_age)
data['Age'] = data['Age'].fillna(mean_age)

# convert columns 'Sex' from string to integer
print(data['Sex'].unique())
data.loc[data['Sex']=='male', "Sex"] = 0
data.loc[data['Sex']=='female', "Sex"] = 1
print(data['Sex'].unique())

print(data['Embarked'].unique())
data['Embarked'] = data['Embarked'].fillna('S')
print(data['Embarked'].unique())
data.loc[data['Embarked'] == 'S','Embarked'] = 0
data.loc[data['Embarked'] == 'C','Embarked'] = 1
data.loc[data['Embarked'] == 'Q','Embarked'] = 2

#print(data['Embarked'].value_counts().sort_index())
# convert columns ''

print(data.head())

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold

print(data.columns)

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
#features = ['Pclass', 'Sex', 'Age','Embarked']


kf = KFold(n_splits=3, random_state=1, shuffle=False)

# drop column because toom many NA
#data = data.drop('Cabin', axis=1)
predictions = []

#print(data[features].describe())

from sklearn.preprocessing import StandardScaler

print('\nstart trainning....')

def test_acc():
    data[features] = data[features].astype(float)
    x_train = data[features]
    y_train = data.Survived
    x_train = StandardScaler().fit_transform(x_train, y_train)
   
    alg = LinearRegression()
    alg.fit(x_train, y_train)
    y_pred = alg.predict(x_train)
    y_pred[y_pred > 0.5] = 1
    y_pred[y_pred <= 0.5] = 0
    acc = sum(y_pred[y_pred==y_train])/len(y_pred)
    print('acc123:', acc)

test_acc()

for train_index, test_index in kf.split(data[features]):
    alg = LinearRegression()
    X_train_data = data[features].iloc[train_index, :]
    y_train_data = data.Survived.iloc[train_index]

    alg.fit(X_train_data, y_train_data)

    X_test_data = data[features].iloc[test_index, :]
    y_test_data = data.Survived.iloc[test_index]

    y_pred = alg.predict(X_train_data)
    predictions.append(y_pred)

    y_pred[y_pred > 0.5] = 1
    y_pred[y_pred <= 0.5] = 0
    
    acc = sum(y_pred[y_pred == y_train_data])/len(y_pred)
    print('acc:', acc)

    # logistic regression
    #lr = LogisticRegression(penalty='l2', C=0.01, solver='lbfgs')
    #lr.fit(X_train_data, y_train_data.values.ravel())
    #yy = lr.predict(X_test_data)
    #yy[y_pred > 0.5] = 1
    #yy[y_pred <= 0.5] = 0
    
    #acc = sum(yy[yy == y_test_data])/len(y_pred)
    #print('acc:', acc)



#predictions = np.concatenate(predictions, axis=0)

#print(type(predictions), predictions.shape)

#predictions[predictions > 0.5] = 1
#predictions[predictions <= 0.5] = 0

