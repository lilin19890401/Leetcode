# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def findMinAndMax(L):
    if len(L) == 0:
        return (None,None)
    min = L[0]
    max = L[0]
    for i in L:
        if i <= min:
            min = i
        if i >= max:
            max = i
    
    return (min,max)

#测试
if findMinAndMax([]) != (None,None):
    print('failed!')
elif findMinAndMax([7]) != (7,7):
    print('failed!')
elif findMinAndMax([7,1]) != (1,7):
    print('failed!')
elif findMinAndMax([7,1,3,9,5]) != (1,9):
    print('failed!')
else:
    print('SUCCESS!!!')