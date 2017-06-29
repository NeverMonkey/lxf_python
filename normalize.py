#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def muti(x, y):
        return x * y
    return reduce(muti, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):

    def f1(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    if '.' in s:
        s0 = s.split('.')[0]
        s1 = s.split('.')[1]
        if s.endswith('.'):
            return reduce(f1, map(char2num, s0))
        elif s.startswith('.'):
            return reduce(f1, map(char2num, s1)) * (0.1 ** len(s1))
        else:
            return reduce(f1, map(char2num, s0)) + reduce(f1, map(char2num, s1)) * (0.1 ** len(s1))
    else:
        return reduce(f1, map(char2num, s))

print('str2float(\'123.456\') =', str2float('123.456'))
print('str2float(\'123.\') =', str2float('123.'))
print('str2float(\'.456\') =', str2float('.456'))
print('str2float(\'789\') =', str2float('789'))