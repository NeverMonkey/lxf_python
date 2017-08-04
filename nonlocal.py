#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func1():
    fs = []
    for i in range(1, 5):
        fs.append(lambda: i * i)
    return fs

f1, f2, f3, f4 = func1()
print(f1(), f2(), f3(), f4())


def func3():
    fs = []
    for i in range(1, 5):
        fs.append(lambda x: i ** x)
    return fs


def func4():
    fs = []
    for i in range(1, 5):
        fs.append(lambda x, i=i: i ** x)
    return fs


f1, f2, f3, f4 = func3()
print(f1(3), f2(3), f3(3), f4(3))
f5, f6, f7, f8 = func4()
print(f5(3), f6(3), f7(3), f8(3))
