
'''
For 3.3, number 4
Use the following equation:
ln(y) = ln(alpha) + n*ln(x)
Raise everything to the e
y = alpha + x(e^n)
'''

import math


def data_set_a():
    data = [[7,8],[14,41],[21,133],[28,250],[35,280],[42,297]]
    return data


def power_function(data):

    n = len(data)

    # How to do ln:
    # math.log()

    # sum(ln(x))
    sum_ln_x = 0

    # sum(x)
    sum_x = 0

    # sum(ln(y))
    sum_ln_y = 0

    # sum(ln(x)*ln(y))
    sum_xy = 0

    # sum(ln(x)**2)
    sum_x2 = 0

    # sum(ln(x)**2 * ln(y))
    sum_x2_y = 0

    for i in range(len(data)):
        sum_ln_x += math.log(data[i][0])
        sum_x += data[i][0]
        sum_ln_y += math.log(data[i][1])
        sum_xy += math.log(data[i][0])*math.log(data[i][1])
        sum_x2 += math.log(data[i][0])**2
        sum_x2_y += math.log(data[i][0])**2 * math.log(data[i][1])

    var_n = (n*sum_xy-sum_ln_x*sum_ln_y)/(n*sum_x2 - sum_x2)

    # var_alpha = math.log((sum_x2_y - sum_xy*sum_ln_x)/(n*sum_ln_x**2 - sum_ln_x**2))
    var_alpha = ((sum_x2_y - sum_xy*sum_ln_x)/(n*sum_x2 - sum_x2))

    return var_n, var_alpha

def create_equation():
    data = data_set_a()

    n, ln_alpha = power_function(data)

    alpha = math.exp(ln_alpha)

    print("N: {} Alpha: {}".format(n,alpha))

    return n, alpha, data

# def main():
#
#     n, alpha = create_equation()
#     print("hello world")
#
#
#
# main()
