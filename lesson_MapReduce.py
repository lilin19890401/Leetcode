# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from functools import reduce
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def normalize(name):
    name = [name[i].lower() for i in range(len(name))]
    name[0] = name[0].upper()
    return ''.join(name)
    
def prod(L):
    return reduce(lambda x,y:x*y,L)
    
def str2float(s):
    """自己的"""
    k = s.find('.')
    fi = reduce(lambda x,y:x*10+y,map(lambda l:DIGITS[l],s[:k]))
    ff = reduce(lambda x,y:x*10+y,map(lambda l:DIGITS[l],s[k+1:]))
    return fi + ff / 10**(len(s)-k-1)

#测试
L1 = ['aDAM','LIsA','barT','hArrY','rON']
L2 = list(map(normalize,L1))
print(L2)
if L2 == ['Adam', 'Lisa', 'Bart', 'Harry', 'Ron']:
    print('\nTest 1 passed!\n')
else:
    print('\nTest 1 failed~\n')


print('3x5x7x9=',prod([3,5,7,9]))
if prod([3,5,7,9]) == 945:
    print('\nTest 2 passed!\n')
else:
    print('\nTest 2 failed~\n')
    

print('str2float(\'123123.456789\') =' ,str2float('123123.456789'))
if abs(str2float('123123.456789') - 123123.456789) < 0.0000001:
    print('\nTest 3 passed!\n')
else:
    print('\nTest 3 failed~\n')
