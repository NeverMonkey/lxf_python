#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3, 4, 8, 9)

# print(f)
# print(type(f()))
# print(type(f))
print(f())


def count1():
    fs = []
    for i in range(1, 5):
        def f():
            return i * i

        fs.append(f)
    ##i = 8
    return fs


f1, f2, f3, f4 = count1()
# print(type(count))
# print(type(count()))
# print(count())
print(f1(), f2(), f3(), f4())


# 返回闭包时牢记的一点就是：
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数
# 用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变


# 此处再创建的函数是f()，用f()的参数‘j’绑定了循环变量‘i’的值，
# f()返回的还是一个函数
# 区别就是此处的‘j’不是循环变量
def count2():
    def f(j):
        # def g():
        #     return j * j
        return lambda: j * j

    fs = []
    for i in range(1, 5):
        fs.append(f(i))
    i = 8
    return fs


f1, f2, f3, f4 = count2()
# print(type(count))
# print(type(count()))
# print(count())
print(f1(), f2(), f3(), f4())



