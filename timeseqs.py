#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date----------------2017-08-17 21:53:08
# @Author--------------Never (nevermonkey@126.com)
# @Link----------------https://github.com/NeverMonkey
# @Host----------------Hasee

import sys
import mytimer
reps = 1000
repslist = range(reps)


def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res


def listComp():
    return [abs(x) for x in repslist]


def mapCall():
    return list(map(abs, repslist))


def genExpr():
    return list(abs(x) for x in repslist)


def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())


print(sys.version)
for tester in (mytimer.timer, mytimer.best):
    print('<{0}>'.format(tester.__name__))
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
        elapsed, result = tester(test)
        # print('-' * 32)
        # print('%-9s:%.5f => [%s....%s]' %
        #       (test.__name__, elapsed, result[0], result[-1]))
        print('#' * 32)
        print('{0:<9}:{1:.5f} => [{2}....{3}]'.format(
            test.__name__, elapsed, result[0], result[-1]))
