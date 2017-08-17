#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date----------------2017-08-17 21:37:00
# @Author--------------Never (nevermonkey@126.com)
# @Link----------------https://github.com/NeverMonkey
# @Host----------------Hasee
"""
Use 3.0 keyword-only default argument instead of ** and dict pops.
no need to hoist range() out of test in 3.0: A generator, not a list
"""
import sys
import time
trace = lambda *args: None  # or print
timefunc = time.clock if sys.platform == 'win32' else time.time


def timer(func, *pargs, _reps=1000, **kargs):
    trace(func, pargs, kargs, _reps)
    start = timefunc()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)


def best(func, *pargs, _reps=50, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best:
            best = time
    return (best, ret)
