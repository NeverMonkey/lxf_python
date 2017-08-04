#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     :   2017-08-04
# @Author       :   NeverMonkey (nevermonkey@126.com)
# @Link     :   https://github.com/NeverMonkey
# @HOST     :   HP


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('Invalid value: %s' % s)
    return 10 / n

foo('0')
