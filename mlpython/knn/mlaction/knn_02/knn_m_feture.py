# coding=utf-8

import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance


features = ['accommodates', 'bedrooms', 'bathrooms', 'beds',
            'price', 'minimum_nights', 'maximum_nights', 'number_of_reviews']

dc_listings = pd.read_csv('listings.csv')

dc_listings = dc_listings[features]

dc_listings['price'] = dc_listings.price.str.replace('\$|,', '').astype(float)
#print('before drapna,', dc_listings.shape)
dc_listings = dc_listings.dropna()
print type(dc_listings)
#print('after drapna,', dc_listings.shape)

dc_listings[features] = StandardScaler().fit_transform(dc_listings[features])

normalize_listings = dc_listings

print normalize_listings.shape

print normalize_listings.head()

# 生成训练集& 测试集
norm_train_df = normalize_listings.copy().iloc[:2792]
norm_test_df = normalize_listings.copy().iloc[2792:]


# 计算欧氏距离
#first_listing = normalize_listings.iloc[0][[]]

# 多变量KNN模型
def predict_price_mul(new_listing_value, features_column):
    temp_df = norm_train_df
    temp_df['distance'] = distance.cdist(temp_df[features_column], [new_listing_value[features_column]])
    temp_df = temp_df.sort_values('distance')
    knn_5 = temp_df.price.iloc[:5]
    pre_price = knn_5.mean()
    return pre_price

cols = ['accommodates', 'bathrooms']
norm_test_df['predicted_price'] = norm_test_df[cols].apply(predict_price_mul, features_column=cols, axis=1)
norm_test_df['squared_error'] = (norm_test_df['predicted_price']-norm_test_df['price'])**2
mse = norm_test_df['squared_error'].mean()
rmse = mse ** (1.0/2.0)
print(rmse)

if __name__ == '__main__':
    pass
