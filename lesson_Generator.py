# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def triangles():
    """自己的答案 """
    L = [1]
    while(True):
        yield L
       
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]
        L.insert(0,1)
        L.append(1)

def triangles1():
    """精妙的答案
    TODO　为何会报错？"""
    L = [1]
    while(True):
        yield L
        L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]


#期待输出
#[1]
#[1,1]
#[1,2,1]
#[1,3,3,1]
#[1,4,6,4,1]
#[1,5,10,10,5,1]
#[1,6,15,20,15,6,1]
#[1,7,21,35,35,21,7,1]
#[1,8,28,56,70,56,28,8,1]
#[1,9,36,84,126,126,84,36,9,1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
        [1],
        [1,1],
        [1,2,1],
        [1,3,3,1],
        [1,4,6,4,1],
        [1,5,10,10,5,1],
        [1,6,15,20,15,6,1],
        [1,7,21,35,35,21,7,1],
        [1,8,28,56,70,56,28,8,1],
        [1,9,36,84,126,126,84,36,9,1],
]:
    print('YOU　SUCCESS!!!')
else:
    print(t)
    print('failed~')