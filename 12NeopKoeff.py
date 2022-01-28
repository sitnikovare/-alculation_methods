import numpy as np

########################################################################################################################

V = T = 1
n = 10
h = T / n

y0 = 0
yn = 0

########################################################################################################################

def X(n, h):
    x = np.zeros(n+1)
    x[0] = 0.0001 #из-за функции fi
    for i in range (1, n+1):
        x[i] = x[i-1] + h
    print(x)
    return x

def P(x):
    return x * x

def Q(x):
    return x

def fi(k, x, T):
    return (x ** k) * (x - T)

def fid1(k, x, T):
    return k * (x ** (k-1)) * (x - T) + (x ** k)

def fid2(k, x, T):
    return k * (k - 1) * (x ** (k-2)) * (x - T) + k * (x ** (k-1)) + k * (x ** (k-1))

def Ak(n, T, x, p, q, f):
    A = np.zeros ((n+1,n+1))
    for i in range (n+1):
        for j in range (n+1):
            A[i][j] = fid2(j+1, x[i], T) + p[i] * fid1(j+1, x[i], T) + q[i] * fi(j+1, x[i], T)

    ak = np.linalg.solve(A, f)
    return ak

def Ycorrect(x, V, T):
    return V * x * x * (x - T)

def F(x, V, T):
    return 4 * V * (x ** 4) - 3 * V * (x ** 3) + 6 * V * x - 2 * V * T

def neoprKoeff(n, T, x, p, q, f):
    a = Ak(n, T, x, p, q, f)
    y = np.zeros(n+1)
    for i in range (n+1):
        for j in range (n+1):
            y[i] += a[i] * fi(j+1, x[i], T)
    print(y)
    return y

def correctSolution(n, x, V, T):
    a = np.zeros(len(x))
    for i in range(len(x)):
        a[i] = Ycorrect(x[i], V, T)
    print(a)
    return a

def error(y, a):
    e = np.zeros(len(y))
    for i in range(len(y)):
        e[i] = y[i] - a[i]
    print(e)
    return e


########################################################################################################################

x = X(n, h)

pk = np.zeros(len(x))
for i in range(len(x)):
    pk[i] = P(x[i])

qk = np.zeros(len(x))
for i in range(len(x)):
    qk[i] = Q(x[i])

fk = np.zeros(len(x))
for i in range(len(x)):
    fk[i] = F(x[i], V, T)

y = neoprKoeff(n, T, x, pk, qk, fk)
ycorr = correctSolution(n, x, V, T)
e = error(y, ycorr)