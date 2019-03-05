import pandas as pd
# import numpy as np




def get_data():
    data = pd.read_csv("9.csv")

    return data

def lagrange(x):

    # print(x)

    a = (19*((x-19)*(x-20)*(x-22))/((17-19)*(17-20)*(17-22)) +25*((x-17)*(x-20)*(x-22))/((19-17)*(19-20)*(19-22))+32*((x-17)*(x-19)*(x-22))/((20-17)*(20-19)*(20-22))+(51*(x-17)*(x-19)*(x-20))/((22-17)*(22-19)*(22-20)))

    # print(a)

    return a

# Lagrange multiplier
def lagrange_least_squares(data):

    least_squares = 0

    for i in range(len(data.index)):

        least_squares += (data.iloc[i,1] - lagrange(data.iloc[i,0]))**2

    return least_squares

def main():

    data = get_data()

    ans = lagrange_least_squares(data)

    print(ans)




main()
