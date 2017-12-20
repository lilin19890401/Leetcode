# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def is_palindrome(n):
    """自己的算法"""
    b = []
    while(n > 0):
        b.append(n % 10)
        n = int(n / 10)
    return b == b[::-1]
def is_palindrome_A(n):
    """精简算法"""
    b = str(n)
    return b == b[::-1]
#测试
output = filter(is_palindrome_A,range(1,10000))
print('1~1000:',list(output))
if list(filter(is_palindrome_A,range(1,200))) == [1,2,3,4,5,6,7,8,9,
       11,22,33,44,55,66,77,88,99,
       101,111,121,131,141,151,161,171,181,191]:
    print('YOU SUCCESS!!!')
else:
    print('you failed~')