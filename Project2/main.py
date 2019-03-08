
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

'''
Convert Data from time to power
Assuming all boats weigh the same, 0lbs
People also weigh nothingq
Are these races consecutive?
It appears that these races are consecutive, the power output is decreasing as consecutive races are ran. Should I take amount of races previously ran into consideration as well as

Velocity Squared * SA * Number of people in the boat

Make an expoential curve b/c it fits the model best. The model should use a linear curve because that is what works best, however we care about a curve of best fit.

'''

def linear_least_squares(x,y,a,b):
    least_squares_criterion_data = 0
    for i in range(len(x)):
        least_squares_criterion_data += (y[i] - a*x[i]+b)**2
        # least_squares_criterion_data += abs(data[i][1] - a + math.exp(b)*data[i][0])**2
    return least_squares_criterion_data

def edit_data():
    data = pd.read_csv("boat_data.csv")

    return data

# def visualize(data):

def time_to_power(data_point, num_people):

    data_split = data_point.split(":")

    # print(num_people)

    # Get number of seconds from minute/seconds representation
    pure_seconds = 60*int(data_split[0]) + int(data_split[1])

    power = (((2500)**3)*(num_people))/((pure_seconds)**3)

    # if (data_point == "16:51" or data_point == "17:25"):
    #     print("Seconds: {} Power: {}".format(pure_seconds,power))

    return power


def get_power():
    data = edit_data()

    # print(data)

    for i in range(len(data.index)):
            for j in range(2,8):
                if (data.iloc[i,j] > '0'):
                    new_data = time_to_power(data.iloc[i,j], data.iloc[i,0])
                    data.iloc[i,j] = new_data

    return data

def power_data():
    data = edit_data()

    # print(data)

    for i in range(len(data.index)):
            for j in range(2,8):
                if (data.iloc[i,j] > '0'):
                    new_data = time_to_power(data.iloc[i,j], data.iloc[i,0])
                    data.iloc[i,j] = new_data
    return data

def main():

    # time_to_power('20:53')

    data = power_data()


    # print(data_a)

    x = []
    y = []

    for i in range(4):
        x.append(data.iloc[i,0])
        y.append(data.iloc[i,2])

    # print(x)
    # print(y)

    a, b = np.polyfit(x,y,1)

    print("A: {} B: {}".format(a,b))

    least_squares = linear_least_squares(x,y,a,b)

    linear_coeffs = np.polyfit(x,y,1)
    linear_function = np.poly1d(linear_coeffs)
    linear_points = linear_function(x)

    print(least_squares)

    # print(linear_points)

    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o", linewidth=0)

    ax.plot(x, linear_points)

    ax.set(xlabel='Rowers in Boat', ylabel='Power',
       title='Power vs. Number of Rowers')
    ax.grid()
    plt.show()


# main()
