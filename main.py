# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from random import randrange

# import the time module
import time


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    right = 0
    total = 0
    while(True):
        total = total + 1
        a = 0
        b = 0
        o = randrange(2)
        op = '+'
        if o == 1:
            op = '+'
            a = randrange(2, 8)
            b = randrange(2, 8)
        else:
            op = '-'
            b = randrange(2, 8)
            a = randrange(b, 8)

        result = -1

        while True:
            try:
                # 👇️ use int() instead of float
                # if you only accept integers
                #countdown(6)
                result = int(input(f'{a} {op} {b} = '))
                break
            except ValueError:
                print('This is not a number, please enter a number:')

        #result = int(input(f'{a} + {b} = ?\n'))
        correct = False
        if op=='+' and a+b == result or op=='-' and a-b==result:
            print("Good Job!")
            right = right + 1
        else:
            while(correct==False):
                while True:
                    try:
                        print("Try again!")
                        result = int(input(f'{a} {op} {b} = '))
                        break
                    except ValueError:
                        print('This is not a number, please enter a number.')
                #result = int(input("Try again!\n"))
                if op=='+' and a+b == result or op=='-' and a-b==result:
                    correct = True
                    print("That is correct!")

        print(f'Your score is {int(right/total * 100)}.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
