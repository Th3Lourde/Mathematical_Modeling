# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 08:51:49 2019

@author: Ryory
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 07:48:08 2019

@author: Ryory
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 07:47:38 2019

@author: Ryory
"""

"""
Author:      Hans de Moor
Created:     December 3, 2018
Python 3.6

Description: This is an illustraton of making a table based on a difference
equation, exporting the table and creating a graph. This is based on Example 2
in Section 1.1, A First Course in Mathematical Modeling by Giordano et al
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

n_months = 9
int_rate = 0.05/12
beg_balance = 4
mo_payment = 5994.18
tbl_first_mo = 0
tbl_last_mo = 9

# Calculations for Example 2 in Section 1.1
balance = np.zeros(n_months + 1)
balance[0] = beg_balance
for n in range(0, n_months):
    # balance[n+1] = int(balance[n]+0.001*balance[n]*(1000-n))
    balance[n+1] = (balance[n]+0.001*balance[n]*(1000-n))

# print(1000-(balance[8]))



# Making and displaying a .cav file with balances for months 61 to 72
b = "{:.2f}"

with open('homemortgage.csv', mode='w', newline="") as hm:
    homemortgage_writer = csv.writer(hm, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)
    for n in range(tbl_first_mo, tbl_last_mo + 1):
        homemortgage_writer.writerow([str(n), b.format(balance[n])])
        print(n, b.format(balance[n]),)

# Creating and displaying a plot similar to Figure 1.6 in Section 1.1
month = np.arange(0, n_months + 1, 1)

fig, ax = plt.subplots()
ax.plot(month, balance)
ax.set(xlabel='Days', ylabel='Rumor Carriers',
       title='Rumor Spread')
ax.grid()
fig.savefig("Rumorspreadgraph.png")
plt.show()
