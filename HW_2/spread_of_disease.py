
'''
Eli Sylvia-Lourde
Mathematical Modeling

Total population: 100,000 residents
Last week there were 18 new cases
The disease lasts three weeks
Everyone has the same odds of being exposed
This week there are 40 new cases
This week, it is estimated that 30% of the existing population is immune because of previous exposure.
'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


def adjust_data(prev_data, new_data_point):

    prev_data[0] = prev_data[1]
    prev_data[1] = new_data_point

    return prev_data

def plot_data(data):

    sns.set()

    f, ax = plt.subplots(1, 1)

    print(data)

    sns.pointplot(ax=ax, x="Week_Number", y="Sick_People", data=data, color=sns.xkcd_rgb["cerulean"])
    sns.pointplot(ax=ax, x="Week_Number", y="Immune_People", data=data, color=sns.xkcd_rgb["violet"])

    ax.legend(handles=ax.lines[::len(data)+1],  labels=["Infected","Immune","Healthy"])

    plt.xlabel('Week')
    plt.ylabel('People')

    plt.show()

def infection(total_pop):

    week_num = 2
    immune = 0
    sick = 58
    vulnerable_pop = total_pop - 18 - 40

    '''
    Newsflash: pretend that the first week has 18 cases

    Correct Constant:
    40 = (100,000 - 100000*0.3 - 18)k
    sick_constant = 0.00057157

    Assume that we are starting at week 3, since we got the data for the first two weeks

    '''

    sick_constant = 0.00057157/15

    # Sick data is the number of people that have the virus
    '''
    sick_data[0] = Week Number
    sick_data[1] = Number of Infected
    sick_data[2] = Number of Immune
    sick_data[3] = Number of Healthy
    '''
    sick_data = [[0,18,0,100000-18],[1,58,0,100000-58]]
    # How many people have the virus to start with

    # Pevious data is the number of people that developed
    # the virus for a given week, where week # is given by
    # the index of the element. Yes, weeks start at zero.
    prev_data = [18,40]


    # while(immune != total_pop):
    while(immune <= total_pop):

        if(week_num >= 2):
            # People can start to get better

            # delta is the number of people that just got the disease this week

            delta = (vulnerable_pop - sick - immune)*(sick_constant)*sick

            # prev_data is the number of people that are now immune

            sick = sick + delta - prev_data[0]


            immune += prev_data[0]

            # These prevent the model from producing unrealistic data-points

            if (immune>100000):
                immune = 100000

            if (sick<0):
                sick = 0

            if (sick>100000):
                sick = 100000

            sick_data.append([week_num, sick, immune, 100000-sick])

            prev_data = adjust_data(prev_data, sick)

            week_num += 1

            if (sick<=0):
                print("Immune: {} Sick: {} Total Pop: {}".format(immune, sick, total_pop))
                break
            if (sick>=100000):
                break


    df = pd.DataFrame(sick_data, columns={'$a':sick_data[0],'$b':sick_data[1],'$c':sick_data[2],'$d':sick_data[3]})

    df.columns = ['Week_Number','Sick_People','Immune_People','Healty_People']

    print(df)

    plot_data(df)

    print("Done")

def main():

    total_pop = 100000
    infection(total_pop)

main()
