
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math


def get_data():
    # biometrical_raw = [[1.75,1.95,1.50,1.75,1.55,1.63,1.71,1.85],[65,85,45,70,48,51,59,75]]

    biometrical_data = [[1.75,65],[1.95,85],[1.50,45],[1.75,70],[1.55,48],[1.63,51],[1.71,59],[1.85,75]]

    df = pd.DataFrame(biometrical_data, columns = ['Height (m)', 'Weight (kg)'])

    # print(df)

    return df


def graph_data(dta):
    sns.set()
    # f, ax = plt.subplots(1, 1)

    g = sns.JointGrid(x="Height (m)", y="Weight (kg)", data=data)
    g = g.plot_joint(plt.scatter, color=".5", edgecolor="blue")
    # g = g.plot_marginals(sns.distplot, kde=False, color="blue")
    # g = g.plot(sns.regplot, sns.distplot)
    # g = g.plot_joint(plt.scatter, color=".5", edgecolor="white")
    # g = g.plot_marginals(sns.distplot, kde=False, color=".5")

    # plt.xlabel('Week')
    # plt.ylabel('People')

    plt.show()
def graph(data):
    sns.set()

    f, ax = plt.subplots(1, 1)

    sns.pointplot(ax=ax, x="Height (m)", y="Weight (kg)", data=data, color=sns.xkcd_rgb["cerulean"])

    g = sns.JointGrid(x="Height (m)", y="Weight (kg)", data=data)
    g = g.plot_joint(plt.scatter, color=".5", edgecolor="blue")
    # g = g.plot_marginals(sns.distplot, kde=False, color="blue")
    # g = g.plot(sns.regplot, sns.distplot)
    # g = g.plot_joint(plt.scatter, color=".5", edgecolor="white")
    # g = g.plot_marginals(sns.distplot, kde=False, color=".5")
    # ax.legend(handles=ax.lines[::len(data)+1],  labels=["Height", ])

    plt.xlabel('Height')
    plt.ylabel('Weight')

    plt.show()


# Generate new data based upon you different equations
# Rank the new data based upon mean sqrs = sum(|y-f(x)|^2)

# pass nx1, sum rows
def e_sum(n):
    ans = 0
    for i in range(len(n)):
        ans += n[i]
    ans /= len(n)
    return ans

def m_error(height, test_height):
    ans = 0
    for i in range(len(height)):
        ans += abs(height[i]-test_height[i])**2
    # print(ans)
    return ans

# W = aH^2
def one(data):
    # ab = []
    a = 0
    test_data = []
    error = []
    # print(len(data['Height (m)']))

    # We want to find a good a value

    h = data['Height (m)']
    w = data['Weight (kg)']

    # One pass to generate a
    for i in range(len(data['Height (m)'])):
        # print(w[i]/(h[i]**2))
        # ab.append(w[i]/(h[i]**2))
        a += w[i]/(h[i]**2)

    # print("\n")

    # print(a)

    a /= len(w)

    # print(a)

    # We now have our equation and can generate our test data points
    for i in range(len(h)):
        test_data.append(a*(h[i]**2))
        test_point = a*(h[i]**2)
        error.append(w[i]-test_point)

    # print(error)

    # ans = m_sum(error)
    ans = m_error(h,test_data)

    print("Equation 1 has least squares error of: {}".format(ans))

# W = aH^2+b
# def two(data):

def main():
    df = get_data()

    one(df)
    # result = test_hypothesis(df)

    # graph(df)
main()
