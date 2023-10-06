# coding=utf-8
####朱+0的功課
####by:WHY/2022.4.17

n = int(input("Input: "))
bool = (0 < n <= 100000) 
if bool == False:
    n = int(input("不符合題目要求，請重新輸入"))
print(n)

lst = [count1, count2, count3, count4, count5, count6] = [0,0,0,0,0,0]

import random 
for t in range(n):
    point = random.randint(1,6)
    lst[point-1] += 1
dice = ["1","2","3","4","5","6"]

import matplotlib.pyplot as plt
plt.bar(dice, lst)
plt.show()
