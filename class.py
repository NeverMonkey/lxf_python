#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print('Cute Animal is running...')


class Dog(Animal):
    def run(self):
        print('Smart Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running Very Slowly...')


class Bird(object):
    def run(self):
        print('Bird is running on the ground')


def run_twice(animal):
    animal.run()
    animal.run()

cat = Cat()
dog = Dog()
cat.run()
dog.run()
print('=' * 64)
run_twice(cat)
run_twice(dog)
run_twice(Tortoise())
print('=' * 64)
run_twice(Bird())
