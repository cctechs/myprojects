# coding=utf-8

from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from scipy.spatial import distance


def predict_price(new_listing_value, feture_column, train_df):
    temp_df = train_df
    temp_df['distance'] = np.abs(temp_df[feture_column]-new_listing_value)
    temp_df = temp_df.sort_values('distance')
    knn_5 = temp_df.price.iloc[:5]
    predicted_price = knn_5.mean()
    return predicted_price


def test_01():
         # 特征
    features = ['accommodates', 'bedrooms', 'bathrooms', 'beds',
                'price', 'minimum_nights', 'maximum_nights', 'number_of_reviews']

    dc_listing = pd.read_csv('listings.csv')

    # 数据筛选
    dc_listing = dc_listing[features]

    # 假设需要预测3的price
    our_acc_value = 3
    dc_listing['distance'] = np.abs(dc_listing.accommodates - our_acc_value)
    print dc_listing.head()
    # 将distance 从小到大的数量计算出来
    dc_listing.distance.value_counts().sort_index()

    # dc_listing.price.value_counts().sort_index()
    dc_listing = dc_listing.sample(frac=1, random_state=0)
    dc_listing = dc_listing.sort_values('distance')
    print dc_listing.price.head()

    dc_listing['price'] = dc_listing.price.str.replace(
        '\$|,', '').astype(float)
    print dc_listing.price.head()
    mean_price = dc_listing.price.iloc[:5].mean()
    print mean_price

    dc_listing.drop('distance', axis=1)

    # 制定好训练集和测试集
    # 打乱顺序
    train_df = dc_listing.copy().iloc[:2792]
    test_df = dc_listing.copy().iloc[2792:]

    for feature in ['accommodates', 'bedrooms', 'bathrooms']:
        test_df['predicted_price'] = test_df.accommodates.apply(
            predict_price, feture_column=feature, train_df=train_df)

        test_df['suqared_error'] = (
            test_df['predicted_price']-test_df['price'])**(2)

        mse = test_df['suqared_error'].mean()
        rmse = mse ** (1.0/2.0)
        print "mes for {} rmse:{}".format(feature, rmse)


def test_02():
    features = ['accommodates', 'bedrooms', 'bathrooms', 'beds',
                'price', 'minimum_nights', 'maximum_nights', 'number_of_reviews']
    dc_listing = pd.read_csv('listings.csv')
    dc_listing = dc_listing[features]
    dc_listing['price'] = dc_listing.price.str.replace(
        '\$|,', '').astype(float)
    dc_listing = dc_listing.dropna()
    dc_listing[features] = StandardScaler().fit_transform(dc_listing[features])
    normalized_listings = dc_listing
    print normalized_listings

    norm_train_df = dc_listing.copy().iloc[:2792]
    norm_test_df = dc_listing.copy().iloc[2792:]

    cols = ['accommodates', 'bathrooms']
    norm_test_df['pre_price'] = norm_test_df[cols].apply(
        predict_price_mul, feature_columns=cols, train_df=norm_train_df, axis=1)

    norm_test_df['suqared_error'] = (
        norm_test_df['predicted_price']-norm_test_df['price'])**(2)

    mse = norm_test_df['suqared_error'].mean()
    rmse = mse ** (1.0/2.0)
    print "mes for {} rmse:{}".format(cols, rmse)


def predict_price_mul(new_list_value, feature_columns, train_df):
    temp_df = train_df
    temp_df['distance'] = distance.euclidean(
        temp_df[feature_columns], [new_list_value[feature_columns]])
    temp_df = temp_df.sort_values['distance']
    knn_5 = temp_df.price.iloc[:5]
    return knn_5.mean()


if __name__ == '__main__':
    # test_01()
    test_02()
