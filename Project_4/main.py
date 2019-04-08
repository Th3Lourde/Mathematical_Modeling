'''
Prompt: Moving Rocks
Evacuating three sites (yield):
A 150
B 400
C 325

Filling four sites (need):
D 175
E 125
F 225
G 450

If we need more dirt:
We can buy dirt from source H at $5 per cubic yard

Cost of shipping dirt = $20 per mile
Amount of dirt being shipped: 10 cubic yards

Table of distances between sources and destinations:

Source     D(5)    E(6)    F(7)     G(8)
A = 1       5       2       6       10
B = 2       4       5       7       5
C = 3       7       6       4       4
H = 4       9       10      6       2

# Equation Needs:
Ax + Bx + Cx =
(D): Ax + By + Cz + Hw <= 175
(E): Ax + By + Cz + Hw <= 125
(F): Ax + By + Cz + Hw <= 225
(H): Ax + By + Cz + Hw <= 450

# Cost:




'''

import pulp as lp

def primal():

    # Create the 'prob' variable to contain all the data
    prob = lp.LpProblem("Test Problem - Primal", lp.LpMinimize)

    x1 = lp.LpVariable("A-D", 0)
    x2 = lp.LpVariable("A-E", 0)
    x3 = lp.LpVariable("A-F", 0)
    x4 = lp.LpVariable("A-G", 0)
    x5 = lp.LpVariable("B-D", 0)
    x6 = lp.LpVariable("B-E", 0)
    x7 = lp.LpVariable("B-F", 0)
    x8 = lp.LpVariable("B-G", 0)
    x9 = lp.LpVariable("C-D", 0)
    x10 = lp.LpVariable("C-E", 0)
    x11 = lp.LpVariable("C-F", 0)
    x12 = lp.LpVariable("C-G", 0)
    x13 = lp.LpVariable("H-D", 0)
    x14 = lp.LpVariable("H-E", 0)
    x15 = lp.LpVariable("H-F", 0)
    x16 = lp.LpVariable("H-G", 0)

    # x1 = lp.LpVariable("A-D", 0, cat="Integer")
    # x2 = lp.LpVariable("A-E", 0, cat="Integer")
    # x3 = lp.LpVariable("A-F", 0, cat="Integer")
    # x4 = lp.LpVariable("A-G", 0, cat="Integer")
    # x5 = lp.LpVariable("B-D", 0, cat="Integer")
    # x6 = lp.LpVariable("B-E", 0, cat="Integer")
    # x7 = lp.LpVariable("B-F", 0, cat="Integer")
    # x8 = lp.LpVariable("B-G", 0, cat="Integer")
    # x9 = lp.LpVariable("C-D", 0, cat="Integer")
    # x10 = lp.LpVariable("C-E", 0, cat="Integer")
    # x11 = lp.LpVariable("C-F", 0, cat="Integer")
    # x12 = lp.LpVariable("C-G", 0, cat="Integer")
    # x13 = lp.LpVariable("H-D", 0, cat="Integer")
    # x14 = lp.LpVariable("H-E", 0, cat="Integer")
    # x15 = lp.LpVariable("H-F", 0, cat="Integer")
    # x16 = lp.LpVariable("H-G", 0, cat="Integer")

    # s1 = lp.LpVariable("Slack 1", 0)
    # s2 = lp.LpVariable("Slack 2", 0)
    # s3 = lp.LpVariable("Slack 3", 0)

    #Set up the objective function
    # prob += 325*x1 + 255*x2 + 342.50*x3, "Total Profit"

    # Cost of moving, each variable is the cost of one truckload.
    # prob += 10*x1 + 4*x2 + 12*x3 + 20*x4 + 8*x5 + 10*x6 + 14*x7 + 10*x8 + 14*x9 + 12*x10 + 8*x11 + 8*x12 + 5*(45*x13 + 50*x14 + 30*x15 + 10*x16) , "Cost of Moving Dirt"

    # Each truck is full of 10 cubic yards of dirt.
    #
    # prob += 100*x1 + 40*x2 + 120*x3 + 200*x4 + 80*x5 + 100*x6 + 140*x7 + 100*x8 + 140*x9 + 120*x10 + 80*x11 + 80*x12 + 50*(180*x13 + 200*x14 + 120*x15 + 40*x16) , "Cost of Moving Dirt"

    # prob += 2*(5*x1 + 2*x2 + 6*x3 + 10*x4 + 4*x5 + 5*x6 + 7*x7 + 5*x8 + 7*x9 + 6*x10 + 4*x11 + 4*x12 + 5*(9*x13 + 10*x14 + 6*x15 + 2*x16)) , "Cost of Moving Dirt"
    prob += 2*5*x1 + 2*2*x2 + 2*6*x3 + 2*10*x4 + 2*4*x5 + 2*5*x6 + 2*7*x7 + 2*5*x8 + 2*7*x9 + 2*6*x10 + 2*4*x11 + 2*4*x12 + (2*9+5)*x13 + (2*10+5)*x14 + (2*6+5)*x15 + (2*2+5)*x16, "Cost of Moving Dirt"
    # Constraints - How much dirt can be shipped from A, B, C:
    # prob += 10*x1 + 10*x2 + 10*x3 + 10*x4 == 150
    # prob += 10*x5 + 10*x6 + 10*x7 + 10*x8 == 400
    # prob += 10*x9 + 10*x10 + 10*x11 + 10*x12 == 325
    '''
    Dual notes:
    Tells you how valuable one of the sources is.

    Take the transpose of rhs of equal signs for constraints --> 7 x 16 matrix
    variable matrix = A
    result matrix = B

    150*y1 + 400*y2 + ... <-- Objective function

    Each row represents a contraint equation

    Multiply by the different constants, weights.

    '''

    # prob += x1 + x2 + x3 + x4 == 150
    # prob += x5 + x6 + x7 + x8 == 400
    # prob += x9 + x10 + x11 + x12 == 325


    prob += x1 + x2 + x3 + x4 == 150
    prob += x5 + x6 + x7 + x8 == 400
    prob += x9 + x10 + x11 + x12 >= 425
    # prob += x9 + x10 + x11 + x12 == 425

    # Constraints - How much dirt can be shipped to D, E, F, G:
    # prob += 10*x1 + 10*x5 + 10*x9 + 10*x13 == 175
    # prob += 10*x2 + 10*x6 + 10*x10 + 10*x14 == 125
    # prob += 10*x3 + 10*x7 + 10*x11 + 10*x15 == 225
    # prob += 10*x4 + 10*x8 + 10*x12 + 10*x16 == 450

    # prob += x1 + x5 + x9 + x13 == 175
    # prob += x2 + x6 + x10 + x14 == 125
    # prob += x3 + x7 + x11 + x15 == 225
    # prob += x4 + x8 + x12 + x16 == 450

    prob += x1 + x5 + x9 + x13 == 175
    prob += x2 + x6 + x10 + x14 == 125
    prob += x3 + x7 + x11 + x15 == 225
    prob += x4 + x8 + x12 + x16 == 450

    # Solve the problem
    prob.solve()

    # Show the status
    print("Status:", lp.LpStatus[prob.status])

    # Show the values of the variables
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    # Show the value of the objective function
    print("Total Cost = ", lp.value(prob.objective))

    return lp.value(prob.objective)

def dual():
    # Create the 'prob' variable to contain all the data
    prob = lp.LpProblem("Test Problem - Dual", lp.LpMaximize)

    y1 = lp.LpVariable("y1", 0)
    y2 = lp.LpVariable("y2", 0)
    y3 = lp.LpVariable("y3", 0)
    y4 = lp.LpVariable("y4", 0)
    y5 = lp.LpVariable("y5", 0)
    y6 = lp.LpVariable("y6", 0)
    y7 = lp.LpVariable("y7", 0)

    #Set up the objective function
    prob += 150*y1 + 400*y2 + 325*y3 + 175*y4 + 125*y5 + 225*y6 + 450*y7, "Total ?"

    prob += y1 + y4 <= 10 , "C1"
    prob += y1 + y5  <= 4 , "C2"
    prob += y1 + y6 <= 12 , "C3"
    prob += y1 + y7 <= 20 , "C4"


    prob +=  y2 + y4 <= 8 , "C5"
    prob +=  y2 + y5 <= 10 , "C6"
    prob +=  y2 + y6 <= 14 , "C7"
    prob +=  y2 + y7 <= 10 , "C8"


    prob +=  y3 + y4 <= 14 , "C9"
    prob +=  y3 + y5 <= 12 , "C10"
    prob +=  y3 + y6 <= 8 , "C11"
    prob +=  y3 + y7 <= 8 , "C12"


    prob += y4 <= 23 , "C13"
    prob += y5 <= 25 , "C14"
    prob += y6 <= 17 , "C15"
    prob += y7 <= 9 , "C16"


    # Solve the problem
    prob.solve()

    # Show the status
    print("Status:", lp.LpStatus[prob.status])

    # Show the values of the variables
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    # Show the value of the objective function
    print("Total ? = ", lp.value(prob.objective))

    return lp.value(prob.objective)


def main():
    a = primal()
    b = dual()
    print("")
    print(a-b-100)
main()
