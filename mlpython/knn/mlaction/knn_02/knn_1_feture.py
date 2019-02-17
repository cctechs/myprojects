# coding=utf-8

import pandas as pd
import numpy as np

def load_data():
    features = ['accommodates','bedrooms','bathrooms','beds','price','minimum_nights','maximum_nights','number_of_reviews']
    dc_listings = pd.read_csv('listings.csv')
    dc_listings = dc_listings[features]
    print dc_listings.head()
    print dc_listings.shape

    # 假设房间数量为3
    our_acc_value = 3
    dc_listings['distance'] = np.abs(dc_listings.accommodates - our_acc_value)
    result = dc_listings.distance.value_counts().sort_index()
    
    # 洗牌
    dc_listings = dc_listings.sample(frac=1, random_state=0)
    dc_listings = dc_listings.sort_values('distance')
    print dc_listings.price.head(0)

    print type(dc_listings.price.str)
    print (dc_listings.price.str)
    dc_listings['price'] = dc_listings.price.str.replace('\$|,','').astype(float)
    print dc_listings.price.head()

    mean_price = dc_listings.price.iloc[:5].mean()
    print mean_price

    dc_listings.drop('distance', axis=1)
    train_df = dc_listings.copy().iloc[:2792]
    test_df = dc_listings.copy().iloc[2792:]

    # 测试结果
    test_df['predicted_price'] = test_df.accommodates.apply(predict_price,train_df=train_df, feature_column='accommodates')
    
    # 计算均方根误差 rmse
    test_df['squared_error'] = (test_df['predicted_price'] - test_df['price'])**(2)
    mse = test_df['squared_error'].mean()
    rmse = mse ** (1.0/2.0)
    print rmse

    # 尝试不同的特征变量，计算rmse
    for f in features:
        test_df['predicted_price'] = test_df[f].apply(predict_price, train_df=train_df, feature_column=f)
        test_df['squared_error'] = (test_df['predicted_price'] - test_df['price'])**(2)
        mse = test_df['squared_error'].mean()
        rmse = mse ** (1.0/2.0)
        print '{} is {}'.format(f,rmse)


# 基于单变量预测价格
def predict_price(new_listing_value, train_df, feature_column):
    temp_df = train_df
    temp_df['distance'] = np.abs(train_df[feature_column] - new_listing_value)
    # 按距离排序
    temp_df = temp_df.sort_values('distance')
    knn_5 = temp_df.price.iloc[:5]
    pre_price = knn_5.mean()
    return pre_price
    

# 测试结果
def test_price():
    pass



if __name__ == '__main__':
    load_data()
