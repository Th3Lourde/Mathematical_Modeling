
"""
Author:      Eli Sylvia-Lourde
Created:     February 13th 2019
Python 3.6

Problems in this file:
1.1 # 9
1.2 # 8
1.3 # 13
"""
import matplotlib.pyplot as plt
import numpy as np
import csv



def prob_9():
    """
    Loan: 30yrs, $200,000, charges 0.5% interest per month
    Loan payments are due every month
    Goal is to clear the loan after 360 payments have occurred


    """

    n_months = 360
    mortgage = 200000 # Initial value
    PV = 200000 # PV of the loan
    int_rate = 0.05/12 # In class, Prof. said that the interest
    # rate should be yearly and not monthly
    mo_payment = 1073.65

    for i in range(360):
        PV = PV + (PV)*(int_rate) - mo_payment

    print(PV)


    # The PV is ~ -5, but this works pretty well besides that
    '''
    Future idea, write an algorithm to solve for the monthly
    payment for me. That would be cool :D
    '''

    print("When the monthly payment is held at ${}, the loan is brought to zero after 360 payments".format(mo_payment))

    '''
    PV = PV + (PV)*(int_rate) - mo_payment
    '''

def decay(num_of_years, current_percent=1):

    decay_per_year = 0.00008771929824561403

    for i in range(num_of_years):
        current_percent = current_percent - current_percent*decay_per_year

        # print(current_percent)

    # Make current_percent a percent

    current_percent = 100*current_percent

    num_as_string = str(current_percent)

    found_num = 0

    percent = ""

    for i in range(len(num_as_string)):

        temp = num_as_string[i]

        if (temp != '0' and temp != '.'):
            found_num += 1

        percent += temp

        if (found_num >= 2):
            break

        # print(num_as_string[i])

    # print(current_percent)

    percent += "%"

    # print(percent)

    return percent

def prob_8():
    '''
    1% of the original amount of carbon-14 remains
    carbon-14 decays at: 50% every 5700 years

    Formulate a model for carbon-14 dating

    Me: If possible, Figure out how old the skull is

    So 0.5 every 5700yrs

    So 8.771929824561403e-05 per year

    My units are in years

    Challenge: Have it generate the answer automatically
    Also have the number of years print out with commas

    '''

    # time = 51999

    time = 37869

    residue = decay(time)

    print(residue)

    print("After {} years, there would be {} left of the skull".format(time,residue))

# n = # of people that know the rumor
def spread_rumor(n, days):

    k = 0.001

    # next_iteration = int(n + (k)*(n)*(1000-n))
    next_iteration = n + (k)*(n)*(1000-n)

    days += 1

    return next_iteration, days

def prob_13():
    '''

    So this time we are modeling how fast a rumor spreads
    we are given how many people there are in the given
    population, how fast the rumor spreads accoring to a
    constant, as well as how many people hear the rumor
    originally. this is modeled by the following equation:

    r_(n+1) = r_n + k*(r_n)*(1000-_n)

    k = 0.001
    n is how many days pass before everyone has heard
    the rumor

    Initially 4 people have heard the rumor

    Might introduce something that will round up (or down)
    the number of people that have heard the rumor

    '''

    infected = 4
    days = 0

    while (infected < 1000):
    # while (infected < 999):
        infected, days = spread_rumor(infected, days)
        print(infected)


    print("After {} days, everyone has heard the rumor".format(days))



def main():

    # prob_9()
    # prob_8()
    prob_13()

    '''
    Don't condense it to % decay per year. Just use unit to figure out when
    it should have decayed to the given percent. Answer is in problem.
    '''





main()
