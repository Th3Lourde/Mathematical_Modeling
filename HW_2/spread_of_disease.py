
'''
Eli Sylvia-Lourde
Mathematical Modeling

Total population: 100,000 residents
Last week there were 18 new cases
The disease lasts three weeks
Everyone has the same odds of being exposed
This week there are 40 new cases
This week, it is estimated that 30% of the existing population is immune because of previous exposure.

The number of infected people surpasses what should actually happen
* Fix the number of people that get infected
* Redo the whole thing b/c it would be faster?


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

    # print(data)

    sns.pointplot(ax=ax, x="Week_Number", y="Sick_People", data=data, color=sns.xkcd_rgb["cerulean"])
    sns.pointplot(ax=ax, x="Week_Number", y="Immune_People", data=data, color=sns.xkcd_rgb["violet"])
    sns.pointplot(ax=ax, x="Week_Number", y="Susceptible_People", data=data, color=sns.xkcd_rgb["kelly green"])

    ax.legend(handles=ax.lines[::len(data)+1],  labels=["Infected","Immune","Susceptible"])

    plt.xlabel('Week')
    plt.ylabel('People')

    plt.show()


def infection(total_pop):

    week_num = 2
    immune = (total_pop-18)*(.3)
    sick = 58
    vulnerable_pop = total_pop - 18 - 40

    '''
    Newsflash: pretend that the first week has 18 cases

    Correct Constant:
    40 = (100,000 - 100000*0.3 - 18)k
    sick_constant = 0.00057157

    Assume that we are starting at week 3, since we got the data for the first two weeks

    '''

    # sick_constant = 0.00057157/15
    sick_constant = 0.00003175174706050264

    # Sick data is the number of people that have the virus
    '''
    sick_data[0] = Week_Number
    sick_data[1] = Sick_People
    sick_data[2] = New_Cases
    sick_data[3] = Immune_People
    sick_data[4] = Got_Better
    sick_data[5] = Susceptible_People
    '''

    sick_data = [[0,18,18,0,0,100000-18],[1,58,40,(total_pop-18)*(.3),(total_pop-18)*(.3),100000-18-((total_pop-18)*(.3))]]

    # Current number of people that are susceptible
    # print(sick_data[week_num-1][-1])

    susceptible = sick_data[1][-1]

    # df.columns = ['Week_Number', 'Sick_People', 'Sick_Delta', 'Immune_People', 'Immune_Delta', 'Susceptible_People']


    # How many people have the virus to start with

    # Pevious data is the number of people that developed
    # the virus for a given week, where week # is given by
    # the index of the element. Yes, weeks start at zero.

    # Change the name of this variable
    # We no longer even need this variable

    prev_data = [18,40]


    # while(immune != total_pop):

    # while(immune <= total_pop):
    while(sick > 0):

        if(week_num >= 2):
            # People can start to get better

            # delta is the number of people that just got the disease this week

            # susceptible = vulnerable_pop - sick - immune
            # susceptible = sick_data[week_num-1][-1]

            # print(susceptible)

            # if (susceptible < 0):
            #     susceptible = 0

            '''
            The number of people that develop the disease is equal to the
            number of people that can get the disease times the number of
            interactions susceptible people have with infected, times the
            probability that one become infected when one interacts with
            someone that is infected
            '''

            delta = (susceptible)*sick_data[week_num-1][1]*(sick_constant)


            # prev_data is the number of people that are now immune

            # if (sick + delta - prev_data[0] < 0):
            #     print("Sick: {} Delta: {} Prev_Data[0]: {}".format(sick, delta, prev_data[0]))

            # sick = sick + delta - prev_data[0]

            # print(sick_data[week_num-1][1])
            # print(delta)
            # print(sick_data[week_num-2][2])

            if (week_num < 3):
                sick = sick_data[week_num-1][1] + delta

            # Last term is for people getting better

            elif (week_num >= 3):
                sick = sick_data[week_num-1][1] + delta - sick_data[week_num-3][2]
                # print(sick_data[week_num-1][1])
                # print(delta)
                # print(sick_data[week_num-3][2])

            # print(sick)

            # print("Prev_Data: {} Sick_Data: {}".format(prev_data[0], sick_data[week_num-3][4]))
            # print(week_num)
            # print("Sick_Data: {}".format(sick_data[week_num-3][4]))


            # immune += prev_data[0]


            if (week_num < 3):
                immune += 0

            if (week_num >= 3):
                immune += sick_data[week_num-3][2]


            # These prevent the model from producing unrealistic data-points

            if (immune>100000):
                immune = 100000

            if (sick<0):
                sick = 0

            if (sick>100000):
                sick = 100000


            if (week_num < 3):

                susceptible = sick_data[week_num-1][-1]-delta

                if (susceptible < 0):
                    susceptible = 0

                # sick_data.append([week_num, sick, delta, immune, 0, sick_data[week_num-1][-1]-delta])

                sick_data.append([week_num, sick, delta, immune, 0, susceptible])

            elif (week_num >= 3):

                susceptible = sick_data[week_num-1][-1]-delta-sick_data[week_num-3][2]

                if (susceptible < 0):
                    susceptible = 0

                sick_data.append([week_num, sick, delta, immune, sick_data[week_num-3][2], susceptible])

            # prev_data = adjust_data(prev_data, sick)

            # Found the bug, was using the number of people that were sick
            # instead of the number of people that just caught the disease

            # prev_data = adjust_data(prev_data, delta)

            week_num += 1

            if (sick<=0):
                # print("Immune: {} Sick: {} Total Pop: {}".format(immune, sick, total_pop))
                break
            if (sick>=100000):
                break


    # df = pd.DataFrame(sick_data, columns={'$a':sick_data[0],'$b':sick_data[1],'$c':sick_data[2],'$d':sick_data[3],'$e':sick_data[4], '$f':sick_data[5]})
    # df = pd.DataFrame(sick_data, columns={'$0':sick_data[0], '$1':sick_data[1], '$2':sick_data[2], '$3':sick_data[3]})
    # df = pd.DataFrame(sick_data, columns={'$a':sick_data[0],'$b':sick_data[1],'$c':sick_data[2],'$d':sick_data[3],'$e':sick_data[4], '$f':sick_data[5]})


    # print(sick_data)



    df = pd.DataFrame(sick_data, columns = ['Week_Number', 'Sick_People', 'New_Cases', 'Immune_People', 'Became_Immune', 'Susceptible_People'])


    # df.rename({'$a':'a', '$b':'b', '$c':'c', '$d':'d', '$e':'e'}, axis='columns')


    print(df)
    #
    # df = df.rename(columns={'0': 'newName1', '1': 'newName2'})


    # df.columns = ['Week_Number', 'Sick_People', 'New_Cases', 'Immune_People', 'Got_Better', 'Susceptible_People']

    # print(df)

    plot_data(df)

    # print("Done")

def main():

    total_pop = 100000
    infection(total_pop)

main()
