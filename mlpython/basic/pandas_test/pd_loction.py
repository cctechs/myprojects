# coding=utf-8

import pandas as pd
data = pd.read_csv('input.csv')
print(data.columns)

print('loc-->')
# location row
print(data.loc[0])
print(data.loc[0, 'cand_pty_affiliation'])
# error
# print(data.loc[0, [5,6]])

print('\niloc-->')
# location only row
print(data.iloc[0])
print(data.iloc[0, [5, 6]])
# error
# print(data.iloc[0, 'cand_pty_affiliation'])

print('\nix-->')
print(data.ix[0])
print(data.ix[0, 'cand_pty_affiliation'])
print(data.ix[0:3, [5, 6]])

print(data.entity_tp.value_counts())
print(data['entity_tp'].value_counts())


df = pd.get_dummies(data.loc[:, 'cand_pty_affiliation'])
print(df.head())



df = pd.get_dummies(data.loc[:, 'entity_tp'])
print(df.head())