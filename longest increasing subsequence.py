# coding=utf-8
####朱+0的功課
####by:WHY/2022.4.17

##輸入值
n = str(input("請輸入一串數字，數字間以空格隔開："))
##轉list[int]
n = n.split(" ")
nums = []
for i in range(len(n)):
    nums.append(int(n[i]))

count_l = [0] * len(nums)
for x in range(len(nums)):
    for l in range(x):
        if nums[l] < nums[x] and count_l[l] >= count_l[x]:
            count_l[x] += 1

import pandas as pd
import numpy as np
df = pd.DataFrame(count_l, columns = ['count_l'])
df.index = nums
print(df)
result = [0]
for y in range(max(count_l)+1):
    small = df.index[df['count_l'] == y].tolist()
    if small[0] > max(result):
        result.append(small[0])
del result[0]
print("length: %d" %len(result))
print("Sequence: ","%s "*len(result) %tuple(result))