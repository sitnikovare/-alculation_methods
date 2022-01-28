import numpy as np

########################################################################################################################

V = 11
x0 = 1
y0 = V
h = 0.01
n = 10

########################################################################################################################

def yfun(x, V):
    if x == 1:
        return V
    return V * x ** 2

def ydif(x, V):
    return 2 * V * x + V * x ** 2 - yfun(x, V)

def ydifimp(x, V):
    return 2 * V * x + V * x ** 2 - (yfun(x - h/2, V) + h/2 * ydif(x - h/2, V))

def ydifpred(x, xpred, V):
    return 2 * V * x + V * x ** 2 - (ydif(xpred, V) + h * ydif(xpred, V))

def euler(x0, h, V, n, y0):
    y = np.zeros(n)
    y[0] = y0
    x = np.zeros(n)
    x[0] = x0

    for i in range (n-1):
        y[i+1] = y[i] + h * ydif(x[i], V)
        if i != n-1:
            x[i+1] = x[i] + h

    a = np.zeros(n)
    for i in range(n):
        a[i] = yfun(x[i], V)

    e = np.zeros(n)
    for i in range(n):
        e[i] = y[i] - a[i]

    #вывод таблицы
    print("Метод Эйлера")
    print(x)
    print(y)
    print(a)
    print(e)

def improvedEuler(x0, h, V, n, y0):
    y = np.zeros(n)
    y[0] = y0
    x = np.zeros(n)
    x[0] = x0

    for i in range (n-1):
        y[i+1] = y[i] + h * ydifimp(x[i] + h/2, V)
        if i != n-1:
            x[i+1] = x[i] + h

    a = np.zeros(n)
    for i in range(n):
        a[i] = yfun(x[i], V)

    e = np.zeros(n)
    for i in range(n):
        e[i] = y[i] - a[i]

    #вывод таблицы
    print("\nУсовершенствованный метод Эйлера")
    print(x)
    print(y)
    print(a)
    print(e)

def predictor(x0, h, V, n, y0):
    y = np.zeros(n)
    y[0] = y0
    x = np.zeros(n)
    x[0] = x0

    for i in range (n-1):
        if i != n-1:
            x[i+1] = x[i] + h
        y[i+1] = y[i] + h/2 * (ydif(x[i], V) + 2 * V * x[i] + V * x[i] ** 2 - yfun(x[i], V))

    a = np.zeros(n)
    for i in range(n):
        a[i] = yfun(x[i], V)

    e = np.zeros(n)
    for i in range(n):
        e[i] = y[i] - a[i]

    #вывод таблицы
    print("\nМетод предиктора-корректора")
    print(x)
    print(y)
    print(a)
    print(e)

########################################################################################################################

euler(x0, h, V, n, y0)
improvedEuler(x0, h, V, n, y0)
predictor(x0, h, V, n, y0)


