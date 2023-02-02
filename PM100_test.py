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
    print("Hello World!")
    # right = 0
    # total = 20
    # errlist = []
    # correctList = []
    # range_min = 2
    # range_max = 8
    # for i in range(total):
    #     print("Q", i+1)
    #     a = 0
    #     b = 0
    #     o = randrange(2)
    #     op = '+'
    #     if o == 1:
    #         op = '+'
    #         a = randrange(range_min, range_max)
    #         b = randrange(range_min, range_max)
    #     else:
    #         op = '-'
    #         b = randrange(range_min, range_max)
    #         a = randrange(b, range_max)
    #
    #     result = -1
    #
    #     while True:
    #         try:
    #             result = int(input(f'{a} {op} {b} = '))
    #             break
    #         except ValueError:
    #             print('This is not a number, please enter a number:')
    #
    #     if op=='+' and a+b == result or op=='-' and a-b==result:
    #         #print("Good Job!")
    #         right = right + 1
    #         question = (a, op, b, result)
    #         correctList.append(question)
    #     else:
    #         question = (a, op, b, result)
    #         errlist.append(question)
    #
    # print('\n*******************************************')
    #
    # print(f'Your score is {int(right/total * 100)}. ')

    # print("============== These answers are correct =================")
    # for j, q in enumerate(correctList):
    #     print(q[0], q[1], q[2], '=', q[3], u'\u2713')
    #
    # print("============== These answers are wrong ===================")
    # for j, q in enumerate(errlist):
    #     print(q[0], q[1], q[2], '=', q[3], u'\u2717')
    #
    # print('*******************************************')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
