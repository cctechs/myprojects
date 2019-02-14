#encoding=utf-8

from __future__ import print_function
import pandas as pd
import numpy as np

print(pd.__version__)

s = pd.Series(['1111', '112', np.nan, '13123'])
print(s)

dates = pd.date_range('20130101', periods=6)
print (dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print (df)


city_names = pd.Series(["San", "San Jose", "Sac"])
population = pd.Series([111, 222, 333])
ss = pd.DataFrame({'CityName': city_names, 'Population': population})
print(ss)

print(city_names.index)


california_housing_dataframe = pd.read_csv("https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")
california_housing_dataframe.describe()
print(california_housing_dataframe)
