import pandas as pd
import numpy as np

'''
This is for ax**3
Also
'''

def least_squares(data,var):
    least_squares_a = 0


    for i in range(len(data.index)):
        # print(data.iloc[i,0])
        # print(a)


        least_squares_a += (data.iloc[i,1] - var*(data.iloc[i,0])**2)**2



    return least_squares_a


def get_data():
    data = pd.read_csv("9.csv")

    return data

def a(data):
    top = 0
    bottom = 0

    # print(data.index)

    # print(len(data.index))

    # print(data.iloc[0,0])

    for i in range(len(data.index)):
    # len(DataFrame.index)
    #
        '''
        This is for ax**2
        '''
        # top += data.iloc[i,0]**(2)*data.iloc[i,1]
        # bottom += data.iloc[i,0]**(2*2)

        '''
        This is for ax**3
        '''
        top += data.iloc[i,0]**(3)*data.iloc[i,1]
        bottom += data.iloc[i,0]**(2*3)
    #
    return top/bottom


def main():
    data = get_data()
    resp = a(data)
    #
    print("A: {}".format(resp))
    #
    resp = least_squares(data,resp)
    #
    print("Least Squares: {}".format(resp))

main()
