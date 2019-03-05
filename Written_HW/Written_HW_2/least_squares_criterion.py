import power_function as pf
import math
import numpy as np

def data_set_a():
    data = [[1.0,3.6],[2.3,3.0],[3.7,3.2],[4.2,5.1],[6.1,5.3],[7.0,6.8]]
    # data = [[0,1.8],[1,3],[2,4.5],[3,7.2],[4,8.5]]
    return data

def data_set_b():

    data = [[29.1,0.0493],[48.2,0.0821],[72.7,0.123],[92.0,0.154],[118,0.197],[140,0.234],[165,0.274],[199,0.328]]

    return data

def data_set_c():

    data = [[2.5,4.32],[3.0,4.83],[3.5,5.27],[4.5,6.26],[4.0,5.74],[5.0,6.76],[5.5,7.23]]

    return data

def data_set_9():

    data = [[17,19],[19,25],[20,32],[22,51],[23,57],[25,71],[28,113],[31,140],[32,153],[33,187],[36,192],[37,205],[39,250],[42,260]]

    return data


def least_squares(data):

    n = len(data)

    # sum(xy)
    xy_sum = 0
    # sum(x)
    x_sum = 0
    # sum(y)
    y_sum = 0
    # sum(x**2)
    x_2_sum = 0
    # sum(y**2)
    y_2_sum = 0

    # Get variables
    for i in range(len(data)):
        xy_sum += data[i][0] * data[i][1]
        x_sum += data[i][0]
        y_sum += data[i][1]
        x_2_sum += data[i][0]**2
        y_2_sum += data[i][1]**2

    # print("Sum x:{}".format(x_sum))
    # print("Sum y:{}".format(y_sum))
    # print("Sum x^2:{}".format(x_2_sum))
    # print("Sum y^2:{}".format(y_2_sum))
    # print("Sum xy:{}".format(xy_sum))


    a = (n*xy_sum-x_sum*y_sum)/(n*x_2_sum - (x_sum)**2)

    b = (x_2_sum*y_sum-xy_sum*x_sum)/(n*x_2_sum-(x_sum)**2)

    return a,b

def least_squares_criterion(data,a,b):
    least_squares_criterion_data = 0
    for i in range(len(data)):
        # least_squares_criterion_data += abs(data[i][1] - a*data[i][0]+b)**2
        least_squares_criterion_data += abs(data[i][1] - a + math.exp(b)*data[i][0])**2
    return least_squares_criterion_data


def linear():

    # data = data_set_a()
    y = []
    x = []
    #
    # for i in range(len(data)):
    #     x.append(data[i][0])
    #     y.append(data[i][1])


    # data = data_set_b()


    # for i in range(len(data)):
    #     x.append(data[i][0])
    #     y.append(data[i][1])


    data = data_set_c()

    data = data_set_9()


    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][1])


    a, b = np.polyfit(x,y,1)





    # Return a, b
    # a,b = least_squares(data)

    # print("Line: {}x+{}".format(a,b))

    least_squares_criterion_data = least_squares_criterion(data,a,b)

    print("Least Squares Criterion: {}".format(least_squares_criterion_data))

    # For data set a
    # a = 0.564
    # b = 2.21

    # For data set b
    # a = 0.00164
    # b = 0.00293

    # For data set c
    # a = 0.98
    # b = 1.855

    # least_squares_criterion_data = least_squares_criterion(data,a,b)
    #
    # print("Least Squares Criterion: {}".format(least_squares_criterion_data))

# def visualize_jkjkj

def main():

    linear()

    # n, alpha, data = pf.create_equation()

    # print("hello n: {}, alpha: {}".format(n, alpha))
    # print(data)

    # least_squares_d = least_squares_criterion(data, alpha, n)

    # print(least_squares_d)

main()
