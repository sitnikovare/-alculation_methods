#Priblizenie mnogochlenom v forme Newtona
import numpy as np

x_true = np.array([0, 1, 2, 3])
f_true = np.array([2, 3, 10, 29])

x_table = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3])

def getRazn(x, y):
    rRazn = [[0] * len(x) for _ in range(len(x))]
    for i in range(len(x)):
        rRazn[i][0] = y[i]

    for i in range(1, len(x)):
        for j in range(i, len(x)):
            rRazn[j][i] = (rRazn[j][i - 1] - rRazn[j - 1][i - 1]) / (x[j] - x[j - i])
    return rRazn

def Newton(x_true, y_true, x0):
    rRazn = getRazn(x_true, y_true)

    lstR = []
    for i in range(len(rRazn)):
        lstR.append(rRazn[i][i])

    result = lstR[0]
    for i in range(1, len(lstR)):
        p = lstR[i]
        for j in range(i):
            p *= (x0 - x_true[j])
        result += p
    return result

rr = getRazn(x_true, f_true)
print('Table:')
rnp = np.array([rr[0], rr[1], rr[2], rr[3]])
print(rnp)
print()

for x in x_table:
    res = Newton(x_true, f_true, x)
    print("N("+ str(x) +") = " + str(res))