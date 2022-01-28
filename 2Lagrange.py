#Priblizenie mnogochlenom v forme Lagranza
import numpy as np

def Lagrange(x, y, x0):
    res = 0.0
    for i in range(len(y)):
        l = y[i]
        for j in range(len(x)):
            if i != j:
                l *= (x0 - x[j]) / (x[i] - x[j])
        res += l
    return res

x_true = np.array([0, 1, 2, 3])
y_true = np.array([2, 3, 10, 29])

x_table = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3])

for i in range(len(x_table)):
    res = Lagrange(x_true, y_true, x_table[i])
    print("Li(" + str(x_table[i]) + ") = " + str(res))