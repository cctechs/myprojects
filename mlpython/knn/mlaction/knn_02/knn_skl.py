#coding=utf-8
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


dc_listings = pd.read_csv('listings.csv')

features = ['accommodates', 'bedrooms', 'bathrooms', 'beds',
            'price', 'minimum_nights', 'maximum_nights', 'number_of_reviews']

dc_listings = dc_listings[features]

dc_listings['price'] = dc_listings.price.str.replace('\$|,','').astype(float)

dc_listings = dc_listings.dropna()


# 数据标准化
dc_listings[features] = StandardScaler().fit_transform(dc_listings[features])

normalized_listings = dc_listings

norm_train_df = normalized_listings.copy().iloc[:2792]
norm_test_df = normalized_listings.copy().iloc[2792:]

print norm_train_df.shape
print norm_test_df.shape

cols = ['accommodates', 'bedrooms']

# 更多特征
#cols = ['accommodates','bedrooms','bathrooms','beds','minimum_nights','maximum_nights','number_of_reviews']

knn = KNeighborsRegressor()

knn.fit(norm_train_df[cols], norm_train_df['price'])
two_features_predictions = knn.predict(norm_test_df[cols])


two_features_mse = mean_squared_error(norm_test_df['price'], two_features_predictions)
two_features_rmse = two_features_mse ** (1.0/2.0)
print(two_features_rmse)


if __name__ == '__main__':
    pass