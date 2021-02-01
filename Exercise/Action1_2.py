# 统计全班的成绩
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

#  输入原始数据
data = {'语文':['68', '95', '98', '90', '80'], '数学':['65', '76', '86', '88', '90'], '英语':['30', '98', '88', '77', '90']}
result = pd.DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])
result.reset_index(inplace=True)
result.rename(columns={'index':'姓名'}, inplace=True)
print(result)
print('\n')

# 更改数据格式（是否有其他方法直接输入的时候定义格式？）
result['语文'] = result['语文'].astype(np.int64)
result['数学'] = result['数学'].astype(np.int64)
result['英语'] = result['英语'].astype(np.int64)

# 进行数据统计
print(result.describe())
print('\n')

# 求和汇总并排序
result['总成绩'] = np.sum(result, axis=1)
result = result.sort_values(['总成绩'], ascending=False)
result['排名'] = result['总成绩'].rank(ascending=False)
print(result)


