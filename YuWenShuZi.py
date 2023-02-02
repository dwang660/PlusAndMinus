#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from random import randrange

# import the time module
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    right = 0
    total = 0
    zh = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    while(True):
        a = randrange(1, 10)

        while True:
            try:
                # 👇️ use int() instead of float
                # if you only accept integers
                #countdown(6)
                result = int(input(zh[a]))
                break
            except ValueError:
                print('This is not a number, please enter a number:')

        correct = False
        if a+1 == result:
            print("Good Job!")
            right = right + 1
        else:
            while(correct==False):
                while True:
                    try:
                        print("Try again!")
                        result = int(input(zh[a]))
                        break
                    except ValueError:
                        print('This is not a number, please enter a number.')
                if a == result:
                    correct = True
                    print("That is correct!")

        #print(f'Your score is {int(right/total * 100)}.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
