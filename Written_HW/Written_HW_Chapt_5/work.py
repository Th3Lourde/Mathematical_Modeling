from random import uniform
from scipy import random
import math
import numpy as np
from random import randint


def func(x):
    return math.sqrt(x)

def main():
    N = 10000
    a = 0.5
    b = 1.5
    xrand = random.uniform(a,b,N)
    good = 0
    total = len(xrand)
    integral = 0.0

    for i in range(N):
        integral += (func(xrand[i]))

    answer = (b-a)/float(N)*integral

    print(answer)


# main()

def rand_int():
    return randint(0,1)


def beach_dayz():
    N = 10002
    # xrand = []
    # for i in range(N):
    #     xrand.append(rand_int())
    # 1 means no rain
    xrand = random.uniform(0,1,N)
    print(xrand)
    good = 0
    streak = 0
    for i in range(N):
        if (xrand[i] >= 0.5):
            xrand[i] = 1
        else:
            xrand[i] = 0


    print(xrand)

    # Now we need to find all 'runs' of rain

    runs = []

    for i in range(N):
        if (xrand[i] == 1):
            runs.append(1)
        if (xrand[i] == 0 and len(runs) > 0):
            if (runs[-1] == 1):
                runs.append(0)


    num_of_threes = 0

    for i in range(len(runs)-3):
        if (runs[i] == 1 and runs[i+1] == 1 and runs[i+2] == 1):
            num_of_threes += 1

    print(num_of_threes)

    print("Number of times it rains for three consecutive days: {}".format(num_of_threes))

    # We care about the number of three day 'sets' that it could have rained for

    print("Number of total 3 Cycles: {}".format(N-2))

    print("{}/{} = {}".format(num_of_threes,(N-2),(num_of_threes)/(N-2)))

# beach_dayz()


def fair_coin():

    a = 0
    b = 1
    N = 100

    c_1 = 0
    c_2 = 0
    c_3 = 0
    c_4 = 0
    c_5 = 0
    c_6 = 0

    xrand = random.uniform(a,b,N)

    for i in range(len(xrand)):
        if (xrand[i] <= 1/6 ):
            c_1 += 1
        elif (xrand[i] <= 2/6 ):
            c_2 += 1
        elif (xrand[i] <= 3/6 ):
            c_3 += 1
        elif (xrand[i] <= 4/6 ):
            c_4 += 1
        elif (xrand[i] <= 5/6 ):
            c_5 += 1
        elif (xrand[i] <= 6/6 ):
            c_6 += 1


    print(c_1)
    print(c_2)
    print(c_3)
    print(c_4)
    print(c_5)
    print(c_6)




fair_coin()





# print(randrange(1/2, 3/2))

# def get_rand_x():
#     return uniform(1/2, 3/2)
#
# def get_rand_y():
#     return uniform(1/2, 3/2)
#
#
#
# def main():
#     numbers_valid = 0
#     total_number = 0
#
#     for i in range(10000000):
#         x = get_rand()
#         y = get_rand()
#         total_number += 1
#         if (y <= math.sqrt(x)):
#             numbers_valid += 1
#
#     print("Monte Carlo Simulation: {}/{} = {}".format(numbers_valid,total_number,numbers_valid/total_number))
#
#
# main()
