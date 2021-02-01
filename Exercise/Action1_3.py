# 对汽车质量数据进行统计
# -*- coding: utf-8 -*-


import pandas as pd

# 读取数据
data = pd.read_csv('D:/OneDrive - 上汽大众汽车有限公司/2021年度/Exercise/car_complain.csv')

# 拆分problem类型至多个字段
data = data.drop('problem', axis=1).join(data.problem.str.get_dummies(','))

# 数据清洗，统一相似品牌名
def clean(x):
    x = x.replace('一汽大众', '一汽-大众')
    return x
data['brand'] = data['brand'].apply(clean)

# 统计各品牌投诉总数
result1 = data.groupby(['brand'])['id'].agg('count')
temp01 = result1

# 重命名
result1 = result1.reset_index()
result1.rename(columns={'brand':'品牌名', 'id':'品牌投诉次数'}, inplace=True)

# 按照“品牌投诉次数”进行排序
result1 = result1.sort_values(['品牌投诉次数'], ascending=False)
result1['排名'] = result1['品牌投诉次数'].rank(ascending=False)
print(result1.loc[:,['品牌名', '品牌投诉次数', '排名']])

# 统计各车型投诉数据并处理格式
result2 = data.groupby(['car_model'])['id'].agg('count')
result2 = result2.reset_index()
result2.rename(columns={'car_model':'车型名', 'id':'车型投诉次数'}, inplace=True)

# 按照“车型投诉次数”进行排序
result2 = result2.sort_values(['车型投诉次数'], ascending=False)
result2['排名'] = result2['车型投诉次数'].rank(ascending=False)
print(result2.loc[:,['车型名', '车型投诉次数', '排名']])

# 统计各品牌的平均车型投诉
temp02 = data.groupby(['brand', 'car_model'])['id'].agg('count')
temp02 = temp02.reset_index()
temp02 = temp02.groupby(['brand'])['id'].agg('count')
model_count = pd.merge(temp01, temp02, left_index=True, right_index=True, how='left')
model_count['平均车型投诉数'] = model_count['id_x'] / model_count['id_y']
model_count.reset_index(inplace=True)
model_count.rename(columns={'brand':'品牌名', 'car_model':'车型名', 'id_x':'车型投诉次数', 'id_y':'车型数'}, inplace=True)

# 按品牌的平均车型投诉排名
model_count = model_count.sort_values(['平均车型投诉数'], ascending=False)
model_count['排名'] = model_count['平均车型投诉数'].rank(ascending=False)
print(model_count)


































