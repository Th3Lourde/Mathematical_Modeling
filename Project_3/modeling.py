from random import randint
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
'''
The idea for this is to roll a d6 and then advance accordingly. We will be using a transition matrix of sorts to get this done.
We will have two variables for every player: number of roles and current square. Number of roles will increase at a constant rate. The current square is based upon the roll of the die as well as the square that the die results on, and whether or not this results in a chute or a ladder.

The curveball for this problem is that the player can only advance to 100 if 100-(their current square) = their roll.
The code for this will be special and will be activate when the players are on square 94+
'''

def roll_d6():
    resp = randint(1, 6)
    return resp

# Index is where the square+roll is.
# square_dict[roll+square] = what square to end up after rolling
square_dict = [0,38, 2,3,14,5,6,7,8,31,10,11,12,13,14,15,6,17,18,19,20,42,22,23,24,25,26,27,84,29,30,31,32,33,34,35,44,37,38,39,40,41,42,43,44,45,46,26,48,11,50,67,52,53,54,55,53,57,58,59,60,61,19,63,60,65,66,67,68,69,70,91,72,73,74,75,76,77,78,79,100,81,82,83,84,85,86,24,88,89,90,91,92,73,94,75,96,97,78,99,100]

def chutes_and_ladders(roll, square):
    # If the player's roll goes beyond the board, nothing happens
    if (square + roll > 100):
        return square
    else:
        return square_dict[square+roll]




def play_game(number_of_games):
    # Number of people
    # Roll psuedo-random die
    # Advance, factor in chute or ladder
    # Keep going until the player reaches the square

    square = 0
    rolls = 0
    roll_data = []
    # number_of_games = 1000


    while (square < 100 and len(roll_data) < number_of_games):

        rolls += 1
        roll = roll_d6()
        temp = square
        square = chutes_and_ladders(roll, square)
        # print("Started at {} rolled {}, went to {}".format(temp,roll,square))

        if (square == 100):
            roll_data.append(rolls)
            rolls = 0
            square = 0



    # print(rolls)
    # print(roll_data)
    ave = 0
    for i in range(len(roll_data)):
        ave += roll_data[i]
    ave /= len(roll_data)
    # print("Ave Rolls: {}".format(ave))
    return ave, roll_data



        # if (square >= 94):
        #     print("special case")


    # Test to make sure that the number is random
    # for i in range(1000):
    #     resp = randint(1, 6)
    #     if (resp <= 0 or resp > 6):
    #         print(resp)

    # Get Roll



def plot_data(data):
    # print(data)

    sns.set()
    f, ax = plt.subplots(1, 1)

    # sns.set(color_codes=True)

    keys = list(data.keys())

    # print(keys)
    # x = np.random.normal(size=100)
    # sns.distplot(x)
    # print(x)

    my_labels = []

    for i in range(len(keys)):
        temp = data[keys[i]][1]
        # print(temp)

        text = "Rolls: {} Ave: {}".format(keys[i], str(round(data[keys[i]][0],3)))

        sns.distplot(temp, kde_kws={"label":text})
        my_labels.append(str(round(data[keys[i]][0],3)))

    # print(my_labels)

    # ax.legend(handles=ax.lines[::len(data)+1],  labels=my_labels)
    # ax.legend(handles=ax.lines[::len(my_labels)+1],  labels=["hello","ther","orls"])


    ax.set(title='Ave Games Played')

    plt.xlabel('Number Of Rolls')
    plt.ylabel('Frequency')
    plt.show()



def main():
    # Get one person to play the game correctly

    data = {}

    start = 10
    for i in range(1,12):
        start *= i
        games = start
        ave, roll_data = play_game(games)
        # print(ave)
        data[start] = [ave, roll_data]

    # print(data)
    plot_data(data)

    # Check to make sure that square_dict is setup correctly:
    # counter_a = 0
    # counter_b = 0
    # for i in range(1, len(square_dict)):
    #     if (square_dict [i] != i):
    #         print("Square {} --> {}".format(i,square_dict[i]))
    #         counter_a += 1
    #     else:
    #         counter_b += 1
    #     # print("Square {} --> {}".format(i,square_dict[i]))
    #
    # print("{} + {} = {}".format(counter_a,counter_b,counter_a+counter_b))
    #

main()
