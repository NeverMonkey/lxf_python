#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_palindrome(n):
    s = str(n)
    # l = len(s)
    # for i in range(l):
    #     if s[i] != s[l-i-1]:
    #         break
    #     else:
    #         return n
    if s == s[::-1]:
        return n


output = filter(is_palindrome, range(1, 100000))
print(list(output))