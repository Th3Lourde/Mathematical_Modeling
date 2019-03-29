
"""
Created on Fri March 29
Author: Eli Sylvia-Lourde


Consumption   Paperback     Quality Paperback     Hardback
paper             3 lb              2                1
ink               2 gal             1                3
prod time        10 min            10               10

Profit           $1                $2               $3

Availability
paper            6000 lb
ink              6000 gal
prod time       22000 minutes

Maximize Profit

Consumption    Artichokes     Lettuce    Cabbage
Irrigation          2           1.6         2.4
Labor              0.75         0.55        0.80
Land                1            1           1


Profit             325          255        342.50

Availability
Irrigation        2,000
Labor             688
Land              1000
"""

import pulp as lp

# Create the 'prob' variable to contain all the data
prob = lp.LpProblem("Test Problem - Primal", lp.LpMaximize)

x1 = lp.LpVariable("Artichokes", 0)
x2 = lp.LpVariable("Lettuce", 0)
x3 = lp.LpVariable("Cabbage", 0)

s1 = lp.LpVariable("Slack 1", 0)
s2 = lp.LpVariable("Slack 2", 0)
s3 = lp.LpVariable("Slack 3", 0)

#Set up the objective function
prob += 325*x1 + 255*x2 + 342.50*x3, "Total Profit"

# Define the constraints
prob += 2*x1 + 1.6*x2 + 2.4*x3 + s1 <= 2000, "Paper consumption limit"
prob += 0.75*x1 + 0.55*x2 + 0.80*x3 + s2 <= 688, "Ink consumption limit"
prob += x1 + x2 + x3 + s3 <= 1000, "Production time limit"

# Solve the problem
prob.solve()

# Show the status
print("Status:", lp.LpStatus[prob.status])

# Show the values of the variables
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Show the value of the objective function
print("Total Profit = ", lp.value(prob.objective))
