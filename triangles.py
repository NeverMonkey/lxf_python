#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def triangles1(max):
    pass



def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[x-1] + L[x] for x in range(1, len(L))] +[1]
'''
m = 0
for f in fib():
    print(f)
    m = m + 1
    if m == 8:
        break
'''

m = 0
for t in triangles():
    print(t)
    m = m + 1
    if m == 20:
        break
