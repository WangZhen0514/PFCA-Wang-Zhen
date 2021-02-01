# 求2+4+6+...+100的值
# -*- coding: utf-8 -*-

# while循环
sum1 = 0
i = 2
while i <=100:
    sum1 = sum1+i
    i= i+2
print("方法一(使用while循环)求和为：" + str(sum1))

# for循环
sum2 = 0
for i in range(2, 101, 2):
    sum2 = sum2+i
print("方法二(使用for循环)求和为：" + str(sum2))
