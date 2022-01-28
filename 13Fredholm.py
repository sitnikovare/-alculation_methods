import numpy as np
########################################################################################################################
V = 11
n = 3
l = 1
a = 0
b = 1
N = 10
h = (b - a) / N
########################################################################################################################
def X(n, h):
    x = np.zeros(n+1)
    for i in range (1, n+1):
        x[i] = x[i-1] + h
    return x

def correct(V, x): #точное решение
    return V * x

def ai(x, i):
    return x ** i

def bi(x, i):
    return x ** i

def aik(i, k): #альфа
    return 1 / (i + k + 1)

def yk(V, k): #гамма
    return V * (1 / (3*(k+2)) + 1 / (4*(k+3)) + 1 / (5*(k+4)))

def f(x, V):
    return V * ((4 * x / 3) + (x * x / 4) + (x ** 3 / 5))

def q_slau(V, l, n):
    A = np.zeros((n, n))
    B = np.zeros(n)

    for k in range (1, n+1):
        A[k-1, 0] = 1
        for i in range (1,n+1):
            A[k-1, i-1] = l / aik(i, k)
            if (k == i):
                A[k-1, i-1] += 1

    for k in range (n):
        B[k] = yk(V, k)

    qk = np.linalg.solve(A, B)

    return qk

def y_solve(x, n, q, l):
    sum = 0
    for i in range (0, n):
        sum += q[i] * ai(x, i+1)

    sum *= l
    return f(x, V) - sum
########################################################################################################################

x = X(N, h)
y = np.zeros(N)
q = q_slau(V, l, n)

for i in range (N):
    y[i] = y_solve(x[i], n, q, l)

corr = np.zeros(N)
for i in range (N):
    corr[i] = correct(V, x[i])

err = np.zeros(N)
for i in range (N):
    err[i] = abs(corr[i] - y[i])

print(x)
print(y)
print(corr)
print(err)
