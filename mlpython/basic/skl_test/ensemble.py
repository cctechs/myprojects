# coding=utf-8

from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
SEED = 222
np.random.seed(SEED)

df = pd.read_csv('./data/input.csv')
print(df.head())
print(df.shape)

print(df.cand_pty_affiliation.value_counts())

df.loc[df.cand_pty_affiliation == 'REP', 'cand_pty_affiliation'] = 1
df.loc[df.cand_pty_affiliation == 'DEM', 'cand_pty_affiliation'] = 0

print(df.cand_pty_affiliation.value_counts())


def get_train_test(test_size=0.95):
    y = df.cand_pty_affiliation
    X = df.drop(['cand_pty_affiliation'], axis=1)
    X = pd.get_dummies(X, sparse=True)
    # remove same value on column
    X.drop(X.columns[X.std() == 0], axis=1, inplace=True)
    return train_test_split(X, y, test_size=test_size)


X_train, x_test, y_train, y_test = get_train_test()
print(X_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

'''
df.cand_pty_affiliation.value_counts(normalize=True).plot(kind='bar', title='123')
plt.show()
'''

from sklearn.tree import DecisionTreeClassifier
t1 = DecisionTreeClassifier(max_depth=1, random_state=SEED)
t1.fit(X_train, y_train)
p = t1.predict_proba(x_test)[:, 1]
print('t1 dt score:', roc_auc_score(y_test, p))


t2 = DecisionTreeClassifier(max_depth=3, random_state=SEED)
t2.fit(X_train, y_train)
p = t2.predict_proba(x_test)[:, 1]
print('t2 dt score:', roc_auc_score(y_test, p))


