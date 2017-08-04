#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 题 1
# 检查密码规则合法性
# 考察基本编码能力和字符串处理
# 参考 python 文档的字符串库

# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10

def valid_password(pwd):
    if len(pwd) >= 2 and len(pwd) <= 10:
        if pwd[0].isalpha():
            if pwd[-1].isdigit() or pwd[-1].isalpha():
                for i in pwd:
                    if i.isalpha() or i.isdigit() or i == '_':
                        return True
    else:
        return False
print(valid_password('Hello'))
print(valid_password('valid_password'))

# 题 2
# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用

def prime_numbers():
    l = [2]
    i = 0
    while i <= 100:
        if i % l[-1] >0:
            l.append(i)
        i = i + 1
    return l

prime_numbers()


# 题 3
# 给定一个只包含字母的字符串，返回单个字母出现的次数
# 考察字典的概念和使用
# 返回值为包含元组的列表，格式如下（对列表中元组的顺序不做要求）
# 参数 "hello"
# 返回值 [('h', 1), ('e', 1), ('l', 2), ('o', 1)]

def letter_count(str):
    pass



# 题 4
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式

def cap_string(str):
    pass



# 题 5
# 写一个 Queue 类，它有两个方法，用法如下
class Queue():
    pass
    def enqueue(self,*args):
        pass
    def dequeue(self):
        pass


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3
