# encoding=utf-8
# https://blog.csdn.net/qq_33758867/article/details/87794848
# 数据处理及可视化
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 算法
from xgboost.sklearn import XGBRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
# 训练
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

#import seaborn as sns

train_data = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')
sample_submission = pd.read_csv('./data/sample_submission.csv')


# sns.distplot(train_data.SalePrice)
#sns.distplot(np.log(train_data.SalePrice + 1))
# plt.show()

# 缺失值填充
# all data
all_data = pd.concat((train_data.drop(["SalePrice"], axis=1), test_data))
all_data_na = (all_data.isnull().sum() / len(all_data)) * 100
print('missing data:', all_data_na)
all_data_na = all_data_na.drop(
    all_data_na[all_data_na == 0].index).sort_values(ascending=False)
plt.figure(figsize=(12, 6))
plt.xticks(rotation="90")
sns.barplot(x=all_data_na.index, y=all_data_na)
# plt.show()

y = train_data['SalePrice']
y = np.log(y+1)

# PoolQC
test_data.loc[960, "PoolQC"] = "Fa"
test_data.loc[1043, "PoolQC"] = "Gd"
test_data.loc[1139, "PoolQC"] = "Fa"

# Garage
test_data.loc[666, "GarageYrBlt"] = 1979
test_data.loc[1116, "GarageYrBlt"] = 1979

test_data.loc[666, "GarageFinish"] = "Unf"
test_data.loc[1116, "GarageFinish"] = "Unf"

test_data.loc[1116, "GarageCars"] = 2
test_data.loc[1116, "GarageArea"] = 480

test_data.loc[666, "GarageQual"] = "TA"
test_data.loc[1116, "GarageQual"] = "TA"

test_data.loc[666, "GarageCond"] = "TA"
test_data.loc[1116, "GarageCond"] = "TA"

# PoolQC
train_data = train_data.fillna({"PoolQC": "None"})
test_data = test_data.fillna({"PoolQC": "None"})

# Alley
train_data = train_data.fillna({"Alley": "None"})
test_data = test_data.fillna({"Alley": "None"})

# FireplaceQu
train_data = train_data.fillna({"FireplaceQu": "None"})
test_data = test_data.fillna({"FireplaceQu": "None"})

# LotFrontage
train_data = train_data.fillna({"LotFrontage": 0})
test_data = test_data.fillna({"LotFrontage": 0})

# Garage
train_data = train_data.fillna({"GarageType": "None"})
test_data = test_data.fillna({"GarageType": "None"})

train_data = train_data.fillna({"GarageYrBlt": 0})
test_data = test_data.fillna({"GarageYrBlt": 0})

train_data = train_data.fillna({"GarageFinish": "None"})
test_data = test_data.fillna({"GarageFinish": "None"})

test_data = test_data.fillna({"GarageCars": 0})
test_data = test_data.fillna({"GarageArea": 0})

train_data = train_data.fillna({"GarageQual": "None"})
test_data = test_data.fillna({"GarageQual": "None"})

train_data = train_data.fillna({"GarageCond": "None"})
test_data = test_data.fillna({"GarageCond": "None"})

# Bsmt
train_data = train_data.fillna({"BsmtQual": "None"})
test_data = test_data.fillna({"BsmtQual": "None"})
train_data = train_data.fillna({"BsmtCond": "None"})
test_data = test_data.fillna({"BsmtCond": "None"})
train_data = train_data.fillna({"BsmtExposure": "None"})
test_data = test_data.fillna({"BsmtExposure": "None"})
train_data = train_data.fillna({"BsmtFinType1": "None"})
test_data = test_data.fillna({"BsmtFinType1": "None"})
train_data = train_data.fillna({"BsmtFinSF1": 0})
test_data = test_data.fillna({"BsmtFinSF1": 0})
train_data = train_data.fillna({"BsmtFinType2": "None"})
test_data = test_data.fillna({"BsmtFinType2": "None"})
test_data = test_data.fillna({"BsmtFinSF2": 0})
test_data = test_data.fillna({"BsmtUnfSF": 0})
test_data = test_data.fillna({"TotalBsmtSF": 0})
test_data = test_data.fillna({"BsmtFullBath": 0})
test_data = test_data.fillna({"BsmtHalfBath": 0})

# MasVnr
train_data = train_data.fillna({"MasVnrType": "None"})
test_data = test_data.fillna({"MasVnrType": "None"})
train_data = train_data.fillna({"MasVnrArea": 0})
test_data = test_data.fillna({"MasVnrArea": 0})

# MiscFeature,Fence,Utilities
train_data = train_data.drop(["Fence", "MiscFeature", "Utilities"], axis=1)
test_data = test_data.drop(["Fence", "MiscFeature", "Utilities"], axis=1)

# other
test_data = test_data.fillna({"MSZoning": "RL"})
test_data = test_data.fillna({"Exterior1st": "VinylSd"})
test_data = test_data.fillna({"Exterior2nd": "VinylSd"})
train_data = train_data.fillna({"Electrical": "SBrkr"})
test_data = test_data.fillna({"KitchenQual": "TA"})
test_data = test_data.fillna({"Functional": "Typ"})
test_data = test_data.fillna({"SaleType": "WD"})


# 探索离群值
train_dummies = pd.get_dummies(pd.concat((train_data.drop(
    ["SalePrice", "Id"], axis=1), test_data.drop(["Id"], axis=1)), axis=0)).iloc[: train_data.shape[0]]
test_dummies = pd.get_dummies(pd.concat((train_data.drop(
    ["SalePrice", "Id"], axis=1), test_data.drop(["Id"], axis=1)), axis=0)).iloc[train_data.shape[0]:]

rr = Ridge(alpha=10)
rr.fit(train_dummies, y)
v = np.sqrt(-cross_val_score(rr, train_dummies, y, cv=5,
                             scoring="neg_mean_squared_error")).mean()
print('v:', v)
y_pred = rr.predict(train_dummies)
resid = y - y_pred
mean_resid = resid.mean()
std_resid = resid.std()
z = (resid - mean_resid)/std_resid
z = np.array(z)
outliers1 = np.where(abs(z) > abs(z).std()*3)[0]
print(outliers1)

er = ElasticNet(alpha=0.001, l1_ratio=0.58)
er.fit(train_dummies, y)
v = np.sqrt(-cross_val_score(er, train_dummies, y, cv=5,
                             scoring="neg_mean_squared_error")).mean()
print("v2:", v)

y_pred = er.predict(train_dummies)
resid = y - y_pred
mean_resid = resid.mean()
std_resid = resid.std()
z = (resid - mean_resid)/std_resid
z = np.array(z)
outliers2 = np.where(abs(z) > abs(z).std()*3)[0]
print(outliers2)

outliers = []
for i in outliers1:
    for j in outliers2:
        if i == j:
            outliers.append(i)

print(outliers)

# 删除离群值
#outliers = np.array(outliers)
# print(type(np.array(outliers)))
print(type(outliers))
print("before drop:", train_data.shape)
train_data = train_data.drop(outliers)
print("after drop:", train_data.shape)

y = train_data['SalePrice']
y = np.log(y+1)

train_dummies = pd.get_dummies(pd.concat((train_data.drop(
    ["SalePrice", "Id"], axis=1), test_data.drop(["Id"], axis=1)), axis=0)).iloc[: train_data.shape[0]]
test_dummies = pd.get_dummies(pd.concat((train_data.drop(
    ["SalePrice", "Id"], axis=1), test_data.drop(["Id"], axis=1)), axis=0)).iloc[train_data.shape[0]:]

# gbr
gbr = GradientBoostingRegressor(max_depth=4, n_estimators=150)
gbr.fit(train_dummies, y)
v = np.sqrt(-cross_val_score(gbr, train_dummies, y, cv=5,
                             scoring="neg_mean_squared_error")).mean()
print('gbr:', v)

# xgb
xgbr = XGBRegressor(max_depth=5, n_estimators=400)
xgbr.fit(train_dummies, y)
v = np.sqrt(-cross_val_score(xgbr, train_dummies, y, cv=5,
                             scoring='neg_mean_squared_error')).mean()
print('xgbr:', v)

# lasso
lsr = Lasso(alpha=0.00047)
lsr.fit(train_dummies, y)
v = np.sqrt(-cross_val_score(lsr, train_dummies, y, cv=5,
                             scoring='neg_mean_squared_error')).mean()
print('lasso:', v)

# ridge
ri = Ridge(alpha=13)
rr.fit(train_dummies, y)
v = np.sqrt(-cross_val_score(ri, train_dummies, y,
                             cv=5, scoring='neg_mean_squared_error')).mean()
print('ridge:', ri)

test_predict = 0.1 * gbr.predict(test_dummies) + 0.3 * xgbr.predict(
    test_dummies) + 0.3 * lsr.predict(test_dummies) + 0.3 * rr.predict(test_dummies)

q1 = pd.DataFrame(test_predict).quantile(0.0042)
pre_df = pd.DataFrame(test_predict)
pre_df["SalePrice"] = test_predict
pre_df = pre_df[["SalePrice"]]
pre_df.loc[pre_df.SalePrice <= q1[0],
           "SalePrice"] = pre_df.loc[pre_df.SalePrice <= q1[0], "SalePrice"] * 0.96
test_predict = np.array(pre_df.SalePrice)
sample_submission["SalePrice"] = np.exp(test_predict)-1
sample_submission.to_csv("./1.csv", index=False)
