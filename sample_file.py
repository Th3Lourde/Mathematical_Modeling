# from math import e
import math

d = [22,28,33,39,44,50,55,61,66,72,77]

v = [20,25,30,35,40,45,50,55,60,65,70]

force = [10,20,30,40,50,60,70,80,90]

stetch = [19,57,94,134,173,216,256,297,343]

y = [6,15,42,114,311,845,2300,6250,17000,46255]

e = [1,2,3,4,5,6,7,8,9,10]

def calc_constant(a,b):
    C = []

    for i in range(len(a)):
        # C.append(a[i]/b[i])
        # C.append((a[i])/(b[i]*b[i]))
        C.append(a[i]/(math.exp(b[i])))
        print(C[i])


calc_constant(y, e)



# for i in range(len(A)):
#     # C.append(A[i]/(B[i]*B[i]))
#     C.append((B[i]*B[i])/A[i])
#
# # print(C)
# for i in range(len(C)):
#     print(C[i])
