
import pandas as pd
import math
import numpy as np



def l_s_10(data,a,b):
    l_s_sum = 0
    for i in range(len(data.index)):
        l_s_sum += (data.iloc[i,1] -a*data.iloc[i,0]**b)**2
    return l_s_sum


def main():
    # data = get_data()

    '''
    for w = aH^b,
    use polyfit(ln(H), ln(w), 1)
    returns a,b

    '''




    d = [[7600000.0,57900000000.0],[19400000.0,108000000000.0],[31600000.0,150000000000.0],[59400000.000000,227999999999.99997],[374000000.0,779000000000.0],[935000000.0,1430000000000.0],[2640000000.0,2870000000000.0],[5220000000.0,4500000000000.0]]

    data = pd.DataFrame(d)


    # print(data.iloc[:,0])



    for i in range(len(data.index)):
        data.iloc[i,0] = math.log(data.iloc[i,0])
        data.iloc[i,1] = math.log(data.iloc[i,1])

    # print(data)

    # print("h: {}, w:{}".format(math.log(data.iloc[:,0]), math.log(data.iloc[:,1])))

    # resp = np.polyfit(math.log(data.iloc[:,0]), math.log(data.iloc[:,1]), 1)
    resp = np.polyfit(data.iloc[:,0], data.iloc[:,1], 1)

    # print(resp)

    resp = l_s_10(data,resp[0],resp[1])

    print(resp)





    # for i in range(len(data.index)):
    #     least_squares_a += (data.iloc[i,1] - (var*(data.iloc[i,0])**3/2))**2


main()
