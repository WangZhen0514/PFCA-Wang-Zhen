# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv('D:/OneDrive - 上汽大众汽车有限公司/2021年度/Exercise/car_complain.csv')
data['brand'] = data['brand'].replace('一汽大众', '一汽-大众')

data_group1 = data.groupby(['brand'])['id'].agg('count')
data_sort1 = data_group1.sort_values(ascending=False)
temp1 = data_sort1
data_sort1 = data_sort1.reset_index()
data_sort1.rename(columns={'brand':'品牌名', 'id':'投诉次数'}, inplace=True)
data_sort1['排名'] = data_sort1['投诉次数'].rank(ascending=False, method='min')
print(data_sort1)

data_group2 = data.groupby(['car_model'])['id'].agg('count')
data_sort2 = data_group2.sort_values(ascending=False)
data_sort2 = data_sort2.reset_index()
data_sort2.rename(columns={'car_model':'车型名', 'id':'投诉次数'}, inplace=True)
data_sort2['排名'] = data_sort2['投诉次数'].rank(ascending=False, method='min')
print(data_sort2)

data_group3 = data.groupby(['brand', 'car_model'])['id'].agg('count')
data_group3 = data_group3.reset_index()
data_group3 = data_group3.groupby(['brand'])['id'].agg('count')
data_group3 = pd.merge(temp1, data_group3, left_index=True, right_index=True, how='left')
data_group3['平均车型投诉数'] = data_group3['id_x'] / data_group3['id_y']
data_group3.reset_index(inplace=True)
data_group3.rename(columns={'brand':'品牌名', 'id_x':'投诉次数', 'id_y':'车型数'}, inplace=True)
data_sort3 = data_group3.sort_values(by='平均车型投诉数', ascending=False)
data_sort3['排名'] = data_sort3['平均车型投诉数'].rank(ascending=False, method='min')
print(data_sort3)

data_sort1.to_excel('D:/OneDrive - 上汽大众汽车有限公司/2021年度/Exercise/car_complain_sort1.xlsx', index=False)
data_sort2.to_excel('D:/OneDrive - 上汽大众汽车有限公司/2021年度/Exercise/car_complain_sort2.xlsx', index=False)
data_sort3.to_excel('D:/OneDrive - 上汽大众汽车有限公司/2021年度/Exercise/car_complain_sort3.xlsx', index=False)