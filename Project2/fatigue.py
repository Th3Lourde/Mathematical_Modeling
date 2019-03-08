import main
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
Predict how people fatigue as they continue to race
'''

# def get_data():
#
#     print(data)

def calc_fatigue():
    data = main.get_power()

    # print(data)
    # print(data.iloc[0,0])

    '''
    Care about how the times get slower and slower
    '''
# diff = [['Race_0'],['Race_1'],['Race_2'],['Race_3']]
    diff = [[],[],[],[]]

    for i in range(len(data.index)):
        for j in range(3,8):
            # print(type(data.iloc[i,j]))
            if (type(data.iloc[i,j]) is not str):
                # print("Previous: {} Current: {}".format(data.iloc[i,j],data.iloc[i,j-1]))
                # print(data.iloc[i,j]-data.iloc[i,j-1])

                # print(data.iloc[i,0])

                diff[i].append((data.iloc[i,j]-data.iloc[i,j-1])/data.iloc[i,0])

        # print("")

    df = pd.DataFrame(diff)
    # df = pd.DataFrame({'A':diff})
    # df = pd.DataFrame({'col':L})

    df = df.rename({0:"Diff_1",1:"Diff_2",2:"Diff_3",3:"Diff_4",4:"Diff_5"}, axis='columns')

    '''
    Make two fatigue equations, one for teams 1-2, another for teams 3-4
    exponential decay for both.
    '''

    # print(df.fillna(0))

    df = df.fillna(0)



    diff_constants = [0]

    for i in range(5):
        constant = 0
        for j in range(4):
            # print(df.iloc[i,j])
            if (df.iloc[j,i] != 'nan'):
                constant += df.iloc[j,i]
        diff_constants.append(constant/4)

        # diff_constants.append(data.iloc[0,i]+)

    # print(diff_constants)


    # A: 104.38298143764881
    # B: -188.03775163057534

    return diff_constants

    # print(data)

def linear_regression(data):
    a = 104.38298143764881
    b = -188.03775163057534
    y = []
    for i in range(len(data)):
        y.append(a*data[i]+b)
    return y

def edit_data():
    data = pd.read_csv("boat_data.csv")

    return data

def data_seconds():
    data = edit_data()

    for i in range(len(data.index)):
            for j in range(2,8):
                # If data != 0
                if (data.iloc[i,j] != '0'):
                    data_split = data.iloc[i,j].split(":")
                    pure_seconds = 60*int(data_split[0]) + int(data_split[1])
                    data.iloc[i,j] = pure_seconds
                if (data.iloc[i,j] == '0'):
                    data.iloc[i,j] = 0
                #     # new_data = time_to_power(data.iloc[i,j], data.iloc[i,0])
                #     data.iloc[i,j] = new_data

    return data

def least_squares_matrix(data,y_hat):

    data = data.astype(np.float)

    least_squares = 0

    for i in range(4):
        for j in range(6):
            # print("Data: {} Y-Hat: {}".format(type((data.iloc[i,j+2])),type(y_hat.iloc[i,j])))
            # print("Data: {} Y-Hat: {}".format(data.iloc[i,j+2],y_hat.iloc[i,j]))
            # print("Data: {} Y-Hat: {}".format(float(data.iloc[i,j+2]),y_hat.iloc[i,j]))
            # least_squares += ((data.iloc[i,j+2])-y_hat.iloc[i,j])^2

            diff = np.subtract(data.iloc[i,j+2], y_hat.iloc[i,j], dtype='float64')

            sqr = np.square(diff)

            least_squares += sqr

            # least_squares += np.subtract(data.iloc[i,j+2], y_hat.iloc[i,j], dtype='float64')

    return least_squares

def graph_differences(data,y_hat):

    data.loc[0,'Race 5'] = 0
    data.loc[0,'Race 6'] = 0
    data.loc[1,'Race 4'] = 0
    data.loc[1,'Race 5'] = 0
    data.loc[1,'Race 6'] = 0

    # print(data)

    # a = 104.38298143764881
    # b = -188.03775163057534
    #
    given = []
    #
    given_1 = []
    given_2 = []
    given_4 = []
    given_8 = []
    #
    # projected = []
    #
    # projected_1 = []
    # projected_2 = []
    # projected_4 = []
    # projected_8 = []
    #
    # Do Given Data
    for j in range(6):
        given_1.append(data.iloc[0,j+2])
        given_2.append(data.iloc[1,j+2])
        given_4.append(data.iloc[2,j+2])
        given_8.append(data.iloc[3,j+2])

    given.append(given_1)
    given.append(given_2)
    given.append(given_4)
    given.append(given_8)

    given = pd.DataFrame(given)

    # print(given_1)

    # print(given)
    print(y_hat)

    x1 = [1,1+2/6,1+3/6,1+4/6,1+5/6,1+5.8/6]
    x2 = [2,2+2/6,2+3/6,2+4/6,2+5/6,2+5.8/6]
    x3 = [3,3+2/6,3+3/6,3+4/6,3+5/6,3+5.8/6]
    x4 = [4,4+2/6,4+3/6,4+4/6,4+5/6,4+5.8/6]


    sns.set()
    f, ax = plt.subplots(1, 1)

    sns.lineplot(x=x1, y=given_1, color=sns.xkcd_rgb["cerulean"])
    sns.lineplot(x=x2, y=given_2, color=sns.xkcd_rgb["cerulean"])
    sns.lineplot(x=x3, y=given_4, color=sns.xkcd_rgb["cerulean"])
    sns.lineplot(x=x4, y=given_8, color=sns.xkcd_rgb["cerulean"])

    sns.lineplot(x=x1, y=y_hat.loc[0,0:5], color=sns.xkcd_rgb["sky blue"])
    sns.lineplot(x=x2, y=y_hat.loc[1,0:5], color=sns.xkcd_rgb["sky blue"])
    sns.lineplot(x=x3, y=y_hat.loc[2,0:5], color=sns.xkcd_rgb["sky blue"])
    sns.lineplot(x=x4, y=y_hat.loc[3,0:5], color=sns.xkcd_rgb["sky blue"])

    # fig, ax = plt.subplots()
    # ax.plot(x1, given_1, marker="o", linewidth=1)
    # ax.plot(x2, given_2, marker="o", linewidth=1)
    #
    # # ax.plot(x, given.iloc[1,:])
    #
    # ax.set(xlabel='Rowers in Boat', ylabel='Power',
    #    title='Power vs. Number of Rowers')
    # ax.grid()

    ax.legend(handles=ax.lines[::len(data)+1],  labels=["Real","Projected"])
    ax.set(title='Power vs. Number of Races')

    plt.xlabel('People In Boat')
    plt.ylabel('Power')
    plt.show()



def compare_to_normal_data():
    # data = edit_data()
    '''
    Seconds is y
    '''
    seconds = data_seconds()
    # print(type(seconds))

    diff_constants = calc_fatigue()

    boys_in_boat = [1,2,4,8]

    y_hat = [[],[],[],[]]

    a = 104.38298143764881
    b = -188.03775163057534

    for i in range(len(boys_in_boat)):
        for j in range(6):
            projected_power = a*boys_in_boat[i]+b - diff_constants[j]
            '''
            Only care about projected power, since it is
            proportional to time
            '''
            y_hat[i].append(projected_power)

            # print("Seconds: {}".format(seconds.iloc[i,j+2]))
            # if (seconds.iloc[i,j+2] != 0):
            #     projected_time = projected_power/seconds.iloc[i,j+2]
            #     y_hat[i].append(projected_time)
            # else:
            #     y_hat[i].append(0)



    y_hat = pd.DataFrame(y_hat)

    print("Y-Hat")
    print(y_hat)

    print("Expected")
    data = main.get_power()

    print(data)

    ls = least_squares_matrix(data,y_hat)

    print(ls)

    graph_differences(data,y_hat)


compare_to_normal_data()
