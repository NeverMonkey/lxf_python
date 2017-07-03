#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an int')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('bith must be a number')
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

s = Student()