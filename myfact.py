#!/usr/bin/env python3
### -*- coding: utf-8 -*-
### @Date----------------2017-08-04 21:33:38
### @Author--------------Never (nevermonkey@126.com)
### @Link----------------https://github.com/NeverMonkey
### @Host----------------Hasee

def fact(n):
    '''

    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

