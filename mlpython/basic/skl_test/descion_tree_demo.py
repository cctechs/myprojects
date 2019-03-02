# coding=utf-8

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from IPython.display import Image
import pydotplus
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cal_housing = np.loadtxt('./CaliforniaHousing/cal_housing.data', delimiter=',')
columns_index = [8, 7, 2, 3, 4, 5, 6, 1, 0]
cal_housing = cal_housing[:, columns_index]

feature_names = ["MedInc", "HouseAge", "AveRooms", "AveBedrms",
                 "Population", "AveOccup", "Latitude", "Longitude"]

target, data = cal_housing[:, 0], cal_housing[:, 1:]

# avg rooms = total rooms / households
data[:, 2] /= data[:, 5]

# avg bed rooms = total bed rooms / households
data[:, 3] /= data[:, 5]

# avg occupancy = population / households
data[:, 5] = data[:, 4] / data[:, 5]

# target in units of 100,000
target = target / 100000.0

print(type(data), type(target))

print(data.shape, target.shape)


X_train, X_test, y_train, y_test = train_test_split(
    data, target, train_size=0.8, test_size=0.2,  random_state=42)
dtr = tree.DecisionTreeRegressor(criterion='mse', max_depth=2, max_features=None,
                                 max_leaf_nodes=None, min_impurity_split=1e-07,
                                 min_samples_leaf=1, min_samples_split=2,
                                 min_weight_fraction_leaf=0.0, presort=False, random_state=None,
                                 splitter='best')

dtr.fit(X_train[:, [6, 7]], y_train)

print(dtr.feature_importances_)

print(dtr.score(X_train[:, [6, 7]], y_train))
print(dtr.score(X_test[:, [6, 7]], y_test))

'''

# visiual tree
dot_data = \
    tree.export_graphviz(
        dtr,
        out_file=None,
        feature_names=feature_names[6:8],
        filled=True,
        impurity=False,
        rounded=True
    )

graph = pydotplus.graph_from_dot_data(dot_data)
graph.get_nodes()[7].set_fillcolor("#FFF2DD")
Image(graph.create_png())

graph.write_png("dtr_white_background.png")

'''

data_train, data_test, target_train, target_test = \
    train_test_split(data, target, test_size=0.1, random_state=42)
dtr = tree.DecisionTreeRegressor(random_state=42)
dtr.fit(data_train, target_train)
s = dtr.score(data_test, target_test)
print('s:', s)


rfr = RandomForestRegressor(random_state=42)
rfr.fit(data_train, target_train)
s = rfr.score(data_test, target_test)
print('ss:', s)

'''
test_param_grid = {'min_samples_split': list((3, 6, 9)),
                   'n_estimators': list((10, 50, 100))}

grid = GridSearchCV(RandomForestRegressor(), param_grid=test_param_grid, cv=5)
grid.fit(data_train, target_train)
print(grid.scorer_, grid.best_params_, grid.best_score_)
'''

rfr = RandomForestRegressor(
    min_samples_split=3, n_estimators=100, random_state=42)
rfr.fit(data_train, target_train)
ss = rfr.score(data_test, target_test)
print('sss:', ss)

df = pd.Series(rfr.feature_importances_, index=feature_names).sort_values()
print(df)
