import numpy as np
########################################################################################################################
V = 11
n = 6
l = 1
a = 0
b = 1
N = 10
h = (b - a) / N
########################################################################################################################
def X(a, b, n):
    # x = np.zeros(n+1)
    # for i in range (1, n):
    #     x[i] = x[i-1] + h
    # return x
    return np.linspace(a, b, n)

def correct(V, x):
    return V * x

def ai(x, i):
    return x ** i

def bi(x, i):
    return x ** i

def aik(i, k):
    return 1 / (i + k + 1)

def yk(V, k):
    return V * (1 / (3*(k+2)) + 1 / (4*(k+3)) + 1 / (5*(k+4)))

def f(x, V):
    return V * ((4 * x / 3) + (x * x / 4) + (x ** 3 / 5))

def Akj(x, t, n):
    a = 0
    for i in range (1, n):
        a += (x ** i) * (t ** i)
    return a

def q_slau(V, l, h, n, x, t):
    A = np.zeros((n-1, n-1))
    B = np.zeros(n-1)

    for k in range (0, n-1):
        A[k, 0] = 1
        for i in range (0,n-1):
            A[k, i] = l * h * Akj(x[k], t[i], n)
            if (k == i):
                A[k, i] += 1

    for k in range (n-1):
        B[k] = f(x[k], V)

    qk = np.linalg.solve(A, B)

    return qk

def y_solve(x, n, q, l):
    sum = 0
    for i in range (0, n-1):
        sum += q[i] * ai(x, i+1)

    sum *= l
    return f(x, V) - sum
########################################################################################################################

x = X(a, b, n)
q = q_slau(V, l, h, n, x, x)

y = np.zeros(n-1)
for i in range (n-1):
    y[i] = y_solve(x[i], n, q, l)

corr = np.zeros(n-1)
for i in range (n-1):
    corr[i] = correct(V, x[i])

err = np.zeros(n-1)
for i in range (n-1):
    err[i] = abs(corr[i] - y[i])

print(x)
print(y)
print(corr)
print(err)
