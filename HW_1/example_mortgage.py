
import matplotlib.pyplot as plt
import numpy as np
import csv

# Problem 9
'''
Your parents are considering a 30-year, $200,000 mortgage that charges 0.5% interest each month.
Formulate a model in terms of a monthly payment p that allows the mortgage (loan) to be paid off after 360 payments. 
Hint: If an represents the amount owed after n months, what are a0 and a360?
'''



n_months = 360
mortgage = 200000
PV = 200000
int_rate = 0.05/12
mo_payment = 1388.89

'''
Each month, the mortgage gets added too based upon the amount of interest it has, and is subtracted based upon how much money you take out
'''

# PV = mortgage + (mortgage)*(int_rate) - mo_payment

# (mortgage)*(int_rate) - mo_payment <-- The change of the mortgage. We want:
# mortgage - change*360 = 0

# I guess we'll guess and check to see what the answer will be. We could totally solve this with math, but I want to finish b4
# class gets out :)

for i in range(360):
    PV = PV + (mortgage)*(int_rate) - mo_payment

print(PV)
