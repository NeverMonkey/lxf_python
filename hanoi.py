#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
将整体分为两部分，一个是n-1，一个是1
'''
s = 0


def hanoi(n, a, b, c):
    global s
    if n == 1:
        s = s + 1
        print('This is the %s step' % s)
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)

hanoi(5, 'A', 'B', 'C')
