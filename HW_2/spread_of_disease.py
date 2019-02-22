
'''
Eli Sylvia-Lourde
Mathematical Modeling
HW 2

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

def plot_data(data):

    sns.set()

    f, ax = plt.subplots(1, 1)

    # Plot each line given the data
    sns.pointplot(ax=ax, x="Week_Number", y="Sick_People", data=data, color=sns.xkcd_rgb["cerulean"])
    sns.pointplot(ax=ax, x="Week_Number", y="Immune_People", data=data, color=sns.xkcd_rgb["violet"])
    sns.pointplot(ax=ax, x="Week_Number", y="Susceptible_People", data=data, color=sns.xkcd_rgb["kelly green"])

    # Add Labels to the different lines
    ax.legend(handles=ax.lines[::len(data)+1],  labels=["Infected","Immune","Susceptible"])

    # Add titles to the x and y axis
    plt.xlabel('Week')
    plt.ylabel('People')

    plt.show()

def infection(total_pop):

    # We are starting at week 2 (Really three b/c start at one)
    # Hardcoding the
    week_num = 2
    immune = (total_pop-18)*(.3)
    sick = 58
    vulnerable_pop = total_pop - 18 - 40

    '''
    Correct Constant:
    40 = (100,000 - 100,000*0.3 - 18)k*18
    sick_constant = 0.000031754197111003146

    Assume that we are starting at week 3, since we got the data for the first two weeks

    '''

    sick_constant = 0.000031754197111003146

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
    susceptible = sick_data[1][-1]

    # Run model while people are still sick
    while(sick > 0):

        # Old case where we had week_num < 2. Taken care of by hard-coding data
        if(week_num >= 2):

            '''
            The number of people that develop the disease is equal to the
            number of people that can get the disease times the number of
            interactions susceptible people have with infected, times the
            probability that one become infected when one interacts with
            someone that is infected
            '''

            delta = (susceptible)*sick_data[week_num-1][1]*(sick_constant)

            # In case the number of people that get infected > those that are susceptible
            if (delta > susceptible):
                delta = susceptible

            # For week 2, people don't get better, so we remove the getting better part
            # of our equation from the graph.

            if (week_num < 3):
                sick = sick_data[week_num-1][1] + delta

            elif (week_num >= 3):
                sick = sick_data[week_num-1][1] + delta - sick_data[week_num-3][2]

            # Same case here

            if (week_num < 3):
                immune += 0

            if (week_num >= 3):
                immune += sick_data[week_num-3][2]

            # These prevent the model from producing unrealistic data-points

            if (immune>100000):
                immune = 100000

            if (sick<0):
                sick = 0

            # This shouldn't happen b/c the number of people that get sick is
            # based upon susceptible people, which should always be < 100000.
            if (sick>100000):
                sick = 100000


            if (week_num < 3):

                susceptible = sick_data[week_num-1][-1]-delta

                # Edge case, shouldn't happen if the model works correctly.
                if (susceptible < 0):
                    susceptible = 0

                sick_data.append([week_num, sick, delta, immune, 0, susceptible])

            elif (week_num >= 3):

                susceptible = sick_data[week_num-1][-1]-delta-sick_data[week_num-3][2]

                if (susceptible < 0):
                    susceptible = 0


                sick_data.append([week_num, sick, delta, immune, sick_data[week_num-3][2], susceptible])

            # Found the bug, was using the number of people that were sick
            # instead of the number of people that just caught the disease

            week_num += 1

            if (int(sick)<=0):
                break
            if (sick>=100000):
                break


    for i in range(len(sick_data)):
        for j in range(len(sick_data[i])):
            sick_data[i][j] = round(sick_data[i][j], 3)

    df = pd.DataFrame(sick_data, columns = ['Week_Number', 'Sick_People', 'New_Cases', 'Immune_People', 'Became_Immune', 'Susceptible_People'])

    plot_data(df)

    # Save Data:
    # df.to_csv(r'Disease_Data.csv')

def main():

    total_pop = 100000
    infection(total_pop)

main()
