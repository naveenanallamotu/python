import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

orders = []
levels = []

def data_fetching(my_data):
    with open(my_data, 'r') as csvfile:
        my_data2 = csv.reader(csvfile)
        next(my_data2)
        for row in my_data2:
            orders.append(int(row[0]))
            levels.append(float(row[1]))
    return


def ploting(orders, levels):
    happy = linear_model.LinearRegression()
    orders = np.reshape(orders, (len(orders), 1))
    levels = np.reshape(levels, (len(levels), 1))
    happy.fit(orders, levels)
    plt.scatter(orders, levels, color='orange')
    plt.plot(orders, happy.predict(orders), color='brown', linewidth=4)
    plt.show()
    return


def gettting(orders, levels, x):
    happy = linear_model.LinearRegression()
    orders = np.reshape(orders, (len(orders), 1))
    levels = np.reshape(levels, (len(levels), 1))
    happy.fit(orders, levels)
    predict_aaa = happy.predict(x)
    return predict_aaa[0][0], happy.coef_[0][0], happy.intercept_[0]


data_fetching("happy.csv")
print(orders,levels)
ploting(orders, levels)

print("values computed for linear regressinon:")
(predict_aaa, coefficient, constant) = gettting(orders, levels, 1)
print("predecting the data", str(predict_aaa))
print("extracting the relation between the order and the data", str(coefficient), str(constant))