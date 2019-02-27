# coding=utf-8
from imblearn.over_sampling import SMOTE
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, recall_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

data = pd.read_csv('creditcard.csv')
columns = data.columns
feature_columns = data.ix[:, data.columns != 'Class']
labels = data.ix[:, data.columns == 'Class']


feature_train, feature_test, label_train, label_test = train_test_split(feature_columns,
                                                                        labels, test_size=0.2, random_state=0)


def printing_KFold_scores(X_train_data, y_train_data):
    fold = KFold(n_splits=5, random_state=0, shuffle=False)
    c_params_range = [0.01, 0.1, 1, 10]

    for c_param in c_params_range:
        print('c_param:', c_param)
        for train_index, test_index in fold.split(y_train_data):

            X_data = X_train_data.iloc[train_index, :]
            y_data = y_train_data.iloc[train_index, :]
            lr = LogisticRegression(C=c_param, penalty='l2', solver='lbfgs')
            lr.fit(X_data, y_data.values.ravel())

            x_test_data = X_train_data.iloc[test_index, :]
            y_test_data = y_train_data.iloc[test_index, :]

            y_preb = lr.predict(x_test_data.values)
            print(y_preb)

            acc = recall_score(y_test_data, y_preb)
            print(acc)


oversmaple = SMOTE(random_state=0)

os_features, os_labels = oversmaple.fit_sample(
    feature_train, label_train.values.ravel())
print(len(os_labels[os_labels == 1]))

os_features = pd.DataFrame(os_features)
os_labels = pd.DataFrame(os_labels)

printing_KFold_scores(os_features, os_labels)
